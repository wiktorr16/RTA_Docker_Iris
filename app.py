import pickle
from math import log10

from flask import Flask
from flask import request
from flask import jsonify
import numpy as np

class Perceptron():
    
    def __init__(self,eta=0.01, n_iter=10):
        self.eta = eta
        self.n_iter = n_iter
    
    def fit(self, X, y):
        self.w_ = np.zeros(1+X.shape[1])
        self.errors_ = []
        
        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X,y):
                update = self.eta*(target-self.predict(xi))
                self.w_[1:] += update*xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self
    
    def net_input(self, X):
        return np.dot(X, self.w_[1:])+self.w_[0]
    
    def predict(self, X):
        return np.where(self.net_input(X)>=0.0,1,-1)

from sklearn import datasets
iris = datasets.load_iris()
X = iris.data[:100,[0,2]]
y = iris.target[:100,]

model = Perceptron()
model.fit(X,y)

app = Flask(__name__)

@app.route('/predict', methods=['GET'])
def get_prediction():

    sepal_length = float(request.args.get('sl'))
    petal_length = float(request.args.get('pl'))
    features = [sepal_length,petal_length]
    
    print(features)
    print(model)
    predicted_class = int(model.predict(features))
    
    return jsonify(features=features, predicted_specie = 'setosa' if predicted_class == -1 else "versicolor")

if __name__ == '__main__':
    app.run(host='0.0.0.0')


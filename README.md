# docker-flask

docker image build -t docker-flask-app .

docker run -p 5000:5000 -d docker-flask-app

localhost:5000/predict?&sl=4.4&pl=1.5

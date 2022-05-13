FROM python:3.8

WORKDIR /docker-flask-ap
COPY . .

RUN pip install Flask jsonify numpy sklearn

CMD ["python","app.py"]
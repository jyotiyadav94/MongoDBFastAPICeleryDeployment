from flask import Flask
from celery import Celery

app = Flask(__name__)

@app.route('/add_numbers')
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)


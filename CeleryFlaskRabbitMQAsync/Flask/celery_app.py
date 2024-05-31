from celery import Celery
from flask import Flask

app = Flask(__name__)
celery = Celery(app.name, broker='amqp://guest:guest@localhost:5672//')
app.config['CELERY_BROKER_URL'] = 'amqp://guest:guest@localhost:5672//'
app.config['RESULT_BACKEND'] = 'rpc://guest:guest@localhost:5672//'

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


@celery.task
def add_numbers(x, y):
    return x + y

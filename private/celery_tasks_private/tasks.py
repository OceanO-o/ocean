from __future__ import absolute_import
from celery_task import Celery


app = Celery('tasks', backend='redis://192.168.60.137:6379/0', broker='amqp://ocean:123456@192.168.60.137:5672//')
# app.conf.update(
#     CELERY_TASK_SERIALIZER='json',
#     CELERY_ACCEPT_CONTENT=['json'],  # Ignore other content
#     CELERY_RESULT_SERIALIZER='json',
#     CELERY_TIMEZONE='Europe/Oslo',
#     CELERY_ENABLE_UTC=True,
# )


@app.task
def add(x, y):
    return x + y


# print("hello")

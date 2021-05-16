from celery import Celery
# from . import celery_conf

celery_app = Celery("fisher")
celery_app.config_from_object('celery_task.celery_conf')

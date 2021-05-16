from celery import Celery

app = Celery("fisher")
app.config_from_object('celery_task.celery_conf')

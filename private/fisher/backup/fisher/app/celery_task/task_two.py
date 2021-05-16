
from . import celery_app
import time

@celery_app.task
def multiply(x, y):
	time.sleep(5)
	return x * y

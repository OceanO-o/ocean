from celery_task import task_one
from celery_task import task_two


task_one.add.delay(2, 4)
task_two.multiply.delay(5, 6)
print('end ......')






# celery 配置文件
BROKER_URL = 'redis://115.159.154.191:6379/1'
CELERY_RESULT_BACKEND = 'redis://115.159.154.191:6379/2'

CELERY_TIMEZONE = 'Asia/Shanghai'

# 导入指定任务模块
CELERY_IMPORTS = (
	'celery_task.task_one',
	'celery_task.task_two'
)

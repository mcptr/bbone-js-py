from celery import current_app
from celery.signals import task_prerun


@task_prerun.connect
def celery_task_prerun(*args, **kwargs):
	current_app.app.app_context().push()

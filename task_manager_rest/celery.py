import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'task_manager_rest.settings')

app = Celery('task_manager_rest')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'every-morning': {
        "task": "email_notifier.tasks.send_daily_email",
        "schedule": crontab(hour=8, minute=0)
    },
    'every-5-minutes': {
        'task': 'email_notifier.tasks.send_deadline_passed_email',
        'schedule': crontab(hour=0, minute='*/5'),
    },
}

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
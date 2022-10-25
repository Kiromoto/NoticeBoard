import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NBoard.settings')

app = Celery('NBoard')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_everyday_9am': {
        'task': 'board.tasks.everyday_mails',
        'schedule': crontab(hour='9', minute='00'),
    },
}

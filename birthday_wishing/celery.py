import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'birthday_wishing.settings')

app = Celery('birthday_wishing')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

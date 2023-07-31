from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from datetime import timedelta

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_project.settings')

APP = Celery('django_celery_project')
APP.conf.enable_utc = False
APP.conf.update(timezone = 'Asia/Kolkata')

# APP.config_from_object('django.conf:settings', namespace='CELERY')
APP.config_from_object(settings, namespace='CELERY')

# Celery Beat Config
APP.conf.beat_schedule ={
    'run-test-every-hour': {
        'task': 'mainapp.task.test_func',
        'schedule': timedelta(seconds=10),  # Run every 3600 seconds (1 hour)
    },
}

# Load task modules from all registered Django app configs.
APP.autodiscover_tasks()


@APP.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
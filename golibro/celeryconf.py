from __future__ import absolute_import, unicode_literals
from os import environ, path
from celery import Celery
from django.conf import settings

golibro = path.basename(path.dirname(__file__))
# set the default Django settings module for the 'celery' program.
environ.setdefault('DJANGO_SETTINGS_MODULE', f'{golibro}.settings')

app = Celery('golibro')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings',  namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

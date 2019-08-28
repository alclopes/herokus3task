from __future__ import absolute_import, unicode_literals
import os
from django.conf import settings
from celery import Celery
from decouple import config

os.environ.setdefault('DJANGO_SETTINGS_MODULE', config('SETTINGS_MODULE_PATH'))

# app = Celery('testheroku', include=['mypage.tasks', 'mycelery.tasks', 'myfile.tasks'])
app = Celery('testheroku')

app.config_from_object('django.conf:settings', namespace='CELERY')

# app.autodiscover_tasks(lambda: [n.name for n in apps.get_app_configs()])
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.update(
    CELERY_TASK_RESULT_EXPIRES=1000,
)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

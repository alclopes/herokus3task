from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import MyFile
import time
import datetime
from django.utils import timezone


# task to delete files and register afetr some time
@shared_task()
def delete_set_task(one_ago):
    # Started task, after 900 seconds / 15 min...
    time.sleep(900)
    # time_ago = datetime.datetime.now() - datetime.timedelta(seconds=900)
    time_ago = timezone.datetime.now() - timezone.timedelta(seconds=900)
    MyFile.objects.filter(created_at__lte=time_ago).delete()
    return True

from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import MyImage
import time
import datetime
from django.utils import timezone


# task to delete images and register after some time
@shared_task()
def delete_set_task(one_ago):
    # Started task, after 900 seconds / 15 min...
    time.sleep(900)
    #time_ago = datetime.datetime.now() - datetime.timedelta(seconds=900)
    time_ago = timezone.datetime.now() - timezone.timedelta(seconds=900)
    MyImage.objects.filter(created_at__lte=time_ago).delete()
    return True

# # Best Practice to task //TODO
# from myapp import app
# from celery.exceptions import SoftTimeLimitExceeded
#
# @app.task
# def mytask():
#     try:
#         do_work()
#     except SoftTimeLimitExceeded:
#         clean_up_in_a_hurry()

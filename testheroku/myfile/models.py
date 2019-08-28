from __future__ import absolute_import, unicode_literals
from django.db.models.signals import post_delete, post_save
from django.db import models
from django.dispatch import receiver
from django.utils import timezone
from django.conf import settings


class MyFile(models.Model):
    description = models.CharField('Name', max_length=80)
    file = models.FileField(
        upload_to='myfile/files', verbose_name='File',
        null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'My File'
        verbose_name_plural = 'My Files'
        ordering = ['-created_at']

    def __str__(self):
        return self.description


# delete the file when your register in the database will be deleted.
@receiver(post_delete, sender=MyFile)
def image_post_delete_handler(sender, **kwargs):
    listingFiles = kwargs['instance']
    storage = listingFiles.file.storage
    if settings.USE_S3:
        path = str(listingFiles.file)
    else:
        path = listingFiles.file.path
    storage.delete(path)

# set task to delete file more later.
@receiver(post_save, sender=MyFile)
def image_post_create_handler(sender, **kwargs):
    from .tasks import delete_set_task
    time_now = timezone.now()
    delete_set_task.apply_async(([1]))



from django.contrib import admin
from .models import MyImage
from .forms import ImageUploadForm


class MyImageAdmin(admin.ModelAdmin):
    form = ImageUploadForm
    model = MyImage


admin.site.register(MyImage)

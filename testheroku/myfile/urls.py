from django.urls import path
from .views import myfile, exclude_files

app_name = 'myfile'

urlpatterns = [
    path('', myfile, name='index'),
    path('cleanimages/', exclude_files, name='exclude_files'),
]


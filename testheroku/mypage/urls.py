from django.urls import path
from .views import mypage, exclude_images

app_name = 'mypage'

urlpatterns = [
    path('', mypage, name='index'),
    path('cleanimages/', exclude_images, name='exclude_images'),
]


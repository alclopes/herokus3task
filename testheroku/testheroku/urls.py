from __future__ import absolute_import, unicode_literals
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from decouple import config

urlpatterns = [
    path('', include('mypage.urls', namespace='mypage')),
    path('myfile/', include('myfile.urls', namespace='myfile')),
    # path('admin/', admin.site.urls),
]

# ##########################Media/Static
USE_S3 = config('USE_S3', default=False, cast=bool)
if settings.DEBUG and not USE_S3:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

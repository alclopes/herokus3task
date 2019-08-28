import os
from .common import *
import dj_database_url
from decouple import config

# ############## DEBUG
DEBUG = config('DEBUG', default=False, cast=bool)

# ############## CELERY

# ############## Servidores autorizados
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])

# ############## DataBase - Heroku
# DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
DATABASES = {'default': dj_database_url.config(conn_max_age=600, ssl_require=True)}
# DATABASE_URL = os.environ['DATABASE_URL']   #VER2019081308


# # ########################## AWS S3 Private Media Upload
if USE_S3:

    # # ########################## AWS S3 - Settings Variable
    AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

    # # ########################## AWS S3 Static files (CSS, JavaScript, Images)
    # # Amazon S3/testheroku-assets/static/myimage/files
    STATICFILES_LOCATION = 'static'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    # STATIC_ROOT = [os.path.join(BASE_DIR, 'mypage/static'), ]  # Não usar com S3
    STATICFILES_STORAGE = 'testheroku.storage_backends.StaticStorage'

    # # ########################## AWS S3 Private Media Upload
    # # Amazon S3/testheroku-assets/media/myimage/files
    MEDIAFILES_LOCATION = 'media'

    # https://testheroku-assets.s3-us-west-2.amazonaws.com/media/myimage/images/Course_6.png
    # AWS_S3_PATH = f'{AWS_STORAGE_BUCKET_NAME}.s3-{AWS_S3_REGION_NAME}.amazonaws.com'   #20190822/0724
    # MEDIA_URL = f'https://{AWS_S3_PATH}/{MEDIAFILES_LOCATION}/'

    # https://testheroku-assets.s3.amazonaws.com/media/myimage/images/Course_6.png
    AWS_S3_PATH = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'  # 20190822/0724
    MEDIA_URL = f'https://{AWS_S3_PATH}/{MEDIAFILES_LOCATION}/'

    # MEDIA_ROOT = os.path.join(BASE_DIR, 'mypage/media') # Não usar com S3
    DEFAULT_FILE_STORAGE = 'testheroku.storage_backends.MediaStorage'


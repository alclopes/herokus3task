import os
from .common import *
from decouple import config

# ############## DEBUG
DEBUG = config('DEBUG_DESENV', default=True, cast=bool)

# ########################## REDIS
CELERY_BROKER_URL = config('REDIS_URL_DESENV')

# ############## CELERY

# ############## Servidores autorizados
ALLOWED_HOSTS = config('ALLOWED_HOSTS_DEV', cast=lambda v: [s.strip() for s in v.split(',')])

# #Apps Instalados
# INSTALLED_APPS += [
#
# ]

# ############## MIDDLEWARE

# Template


# ########################## AWS S3 Private Media Upload
if USE_S3:

    # # ########################## AWS S3 - Settings Variable
    AWS_STORAGE_BUCKET_NAME = config('AWS_STORAGE_BUCKET_NAME_DESENV')
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

























# DATABASES Postgre
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': config('DB_NAME'),
            'USER': config('DB_USER'),
            'PASSWORD': config('DB_PASSWORD'),
            'HOST': config('DB_HOST'),
            'PORT': config('DB_PORT', default=5432),
        }
    }


# # ########################## Static files (CSS, JavaScript, Images)
# STATIC_URL = '/static/'  # aponta para dentro de cada app core
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # Heroku pode servir desde que seja nesta pasta
# STATIC_ROOT = (
#     os.path.join(BASE_DIR, 'static'),
# )


# # ########################## Media
# # Media files are for user-uploaded content.
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

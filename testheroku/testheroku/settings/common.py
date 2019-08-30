from __future__ import absolute_import, unicode_literals
import os
from decouple import config
from django.conf import settings


# ############## BASE_DIR
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(f'BASE_DIR: {BASE_DIR}')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

SECRET_KEY = config('SECRET_KEY')

DEBUG = config('DEBUG', default=False, cast=bool)

# ############## Application definition
INSTALLED_APPS = [
    # 'django.contrib.admin',  # Remover se não precisar para não copiar arquivos para o S3
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_celery_results',
    # MyApps
    'mypage',
    'myfile',
]

ROOT_URLCONF = 'testheroku.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'testheroku.wsgi.application'

# ##############  Database
DATABASES = {}

# ############## MIDDLEWARE
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ########################## # Databases


# ########################## # Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# ##########################  Internationalization
LANGUAGE_CODE = 'en'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# ########################## AWS S3
USE_S3 = config('USE_S3', default=False, cast=bool)
if USE_S3:
    # ############## Application definition - AWS
    INSTALLED_APPS += [
        #S3
        'storages',
    ]

    # # ########################## AWS S3 - Settings Variable
    AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    AWS_S3_REGION_NAME = 'us-west-2'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    AWS_DEFAULT_ACL = None

else:

    # # ########################## Static files (CSS, JavaScript, Images)
    STATIC_URL = '/static/'  # aponta para dentro de cada app core
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') # Heroku pode servir desde que seja nesta pasta
    STATIC_ROOT = (
        os.path.join(BASE_DIR, 'static'),
    )

    # # ########################## Media
    # Media files are for user-uploaded content.
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# ########################## REDIS
CELERY_BROKER_URL = config('REDIS_URL')

# Configurando Celery para rodar em paralelo (True => para testes)
CELERY_TASK_ALWAYS_EAGER = config('CELERY_TASK_ALWAYS_EAGER_DESENV', default=False, cast=bool)
# CELERY_TASK_ALWAYS_EAGER = config('CELERY_TASK_ALWAYS_EAGER', default=False, cast=bool)


# ########################## django-celery-results
CELERY_RESULT_BACKEND = 'django-db'
CELERY_CACHE_BACKEND = 'django-cache'


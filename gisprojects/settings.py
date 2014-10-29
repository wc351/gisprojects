"""
Django settings for gisprojects project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from vendor.generate_key import generate_key

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '{}'.format(generate_key(40, 128))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.projects',
    'bootstrap',
    'vendor.registration',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'gisprojects.urls'

WSGI_APPLICATION = 'gisprojects.wsgi.application'


# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
ABSOLUTE_URL_OVERRIDES = {'auth.user': lambda url: '/'}
LOGIN_REDIRECT_URL = '/'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'gisprojects',
        'USER': 'postgres',
        'PASSWORD': 'geografio',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

DEFAULT_FILE_STORAGE = 'gisprojects.s3utils.MediaRootS3BotoStorage'
STATICFILES_STORAGE = 'gisprojects.s3utils.MediaRootS3BotoStorage'
AWS_ACCESS_KEY_ID = 'AKIAIMO2QEEKUP23MHIA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'gisprojects'
MEDIA_ROOT = 'media/'
STATIC_ROOT = 'static/'
S3_URL = 'http://{}.s3.amazonaws.com/'.format(AWS_STORAGE_BUCKET_NAME)
MEDIA_URL = S3_URL + MEDIA_ROOT
STATIC_URL = S3_URL + STATIC_ROOT


# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,  'templates'),
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "bstatic"),
)
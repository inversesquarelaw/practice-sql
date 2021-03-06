"""
Django settings for FirstSite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y0g%&do%(%zpe&wm!9rn%uk8#)lt_09*4_=s-gj7*+b@r!1!yx'

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
    'mydbapp',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'FirstSite.urls'

WSGI_APPLICATION = 'FirstSite.wsgi.application'

#added template stuff
TEMPLATE_DIRS = {
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    
    '/home/user/code/python/practice-sql/FirstSite/templates/',
}


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'employees',
        'USER': 'mysqluser',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '',
    },
    'salaries': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'salaries',
        'USER': 'mysqluser',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '',
    },
    'departments': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'departments',
        'USER': 'mysqluser',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

#added static stuff
PROJECT_PATH = '/home/user/code/python/practice-sql/FirstSite'
STATIC_PATH = os.path.join(PROJECT_PATH, 'static')
STATICFILES_DIRS = (
    STATIC_PATH,
)

#added media stuff
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media') #absolute path to media

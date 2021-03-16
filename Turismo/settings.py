"""
Django settings for Turismo project.

Generated by 'django-admin startproject' using Django 2.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import cloudinary

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e(ap(#0*o43#5cgyvuz_$+6chi+6)q4z2%#pi&6t=&b&w&i)yl'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'import_export',
    'Apps.deportes',
    'Apps.home',
    'Apps.hoteles',
    'Apps.perfil',
    'Apps.platos',
    'Apps.reservas',
    'Apps.turismos',
    'Apps.usuarios',
    'bootstrap4',
    'smartfields',
    'widget_tweaks',
    'preventconcurrentlogins',
]


MIDDLEWARE = [
    'Apps.usuarios.middleware.PruebaMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_session_timeout.middleware.SessionTimeoutMiddleware',
    'preventconcurrentlogins.middleware.PreventConcurrentLoginsMiddleware',
]
SITE_ID = 1
ROOT_URLCONF = 'Turismo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'Templates')],
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

WSGI_APPLICATION = 'Turismo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases
import dj_database_url
from decouple import config

#esta es la manera normal de conectarse a a las base de datos
"""DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'BDTurismo',
        'USER': 'postgres',
        'PASSWORD': '12345',
        'HOST': '127.0.0.1',
        'DATABASE_PORT': '5432',
    }
}
"""
#esta es la manera de conectarse a la base de datos utilizando dj_database_url cuando ya esta en produccion utilizando heroku
DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
#para crear el modelo user
AUTH_USER_MODEL = 'usuarios.Usuario'
# lineas para caducar la session de
SESSION_EXPIRE_AFTER_LAST_ACTIVITY = True
SESSION_EXPIRE_AFTER_LAST_ACTIVITY_GRACE_PERIOD  =  60
#SESSION_COOKIE_AGE = 30 * 60 # Resultado 5 minutos (Por defecto viene 1209600)
# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True


#lineas de configuracion para envio de correo electrino de confirmacion al crear nuevos usuarios
EMAIL_USE_TLS = True 
EMAIL_HOST = 'smtp.gmail.com' 
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER') 
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD') 
EMAIL_PORT = 587
#fin lineas de configuracion para envio de correo electrino de confirmacion al crear nuevos usuarios

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

STATIC_ROOT = os.path.join(BASE_DIR, "live-static", "static-root")

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

#STATIC_ROOT = "/home/cfedeploy/webapps/cfehome_static_root/"

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "live-static", "media-root")

#para servir archivos media con claudinary
cloudinary.config(
    cloud_name = os.environ.get('CLOUD_NAME'),
    api_key = os.environ.get('API_KEY'),
    api_secret = os.environ.get('API_SECRET'),
    secure = True
)
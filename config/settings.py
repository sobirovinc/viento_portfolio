from pathlib import Path
import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
import dj_database_url


BASE_DIR = Path(__file__).resolve().parent.parent

import environ
env = environ.Env()
env.read_env()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'yt3%05apivq2f0yk!q_hhe154@u$&ou%p%!s92#sz-%gawuhc*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # created
    'main',

    # installed packages
    'rest_framework',

]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': config('DB_NAME'),
#         'USER': config('USER'),
#         'PASSWORD': config('PASSWORD'),
#         'HOST': config('HOST'),
#         'PORT': config('PORT')
#     }
# }
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'vientodb',
#         'USER': 'vientodb_user',
#         'PASSWORD': 'RQhVqVmljVuLgzsBCpWoDGvpjIRMfaB4',
#         'HOST': 'dpg-cjkaa0r37aks7388fmv0-a',
#         'PORT': 5432,
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': dj_database_url.parse('postgres://vientodb_user:RQhVqVmljVuLgzsBCpWoDGvpjIRMfaB4@dpg-cjkaa0r37aks7388fmv0-a.oregon-postgres.render.com/vientodb')
}
# postgres://viento_db_user:bvIbfn4j9YtoEaFr0cE7wUQLuXi1Dzuo@dpg-cjk9j2tk5scs73bqnug0-a/viento_db


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

MEDIA_URL = '/media-files/'
MEDIA_ROOT = 'media-files'

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

TELEGRAM_BOT_TOKEN = '6382435347:AAFZhBYwhpsRIuKIhBPA6HJzOUaJBImyobY'
TELEGRAM_CHAT_ID = '388459048'


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'permissions.AllowAnyPermission',
    ],
}


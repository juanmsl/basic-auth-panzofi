import sys
from os import environ
from os.path import abspath, basename, dirname, join, normpath

DJANGO_ROOT = dirname(dirname(abspath(__file__)))

PROJECT_ROOT = dirname(DJANGO_ROOT)

SECRET_KEY = environ.get(
    'SECRET_KEY',
    'abcdefghijklmnopqrstuvwxyz0123456789!$%&()=+-_'
)

SITE_NAME = basename(DJANGO_ROOT)

STATIC_ROOT = join(PROJECT_ROOT, 'run', 'static')

MEDIA_ROOT = join(PROJECT_ROOT, 'run', 'images')

STATICFILES_DIRS = [
    join(PROJECT_ROOT, 'static'),
]

PROJECT_TEMPLATES = [
    join(PROJECT_ROOT, 'templates'),
]

sys.path.append(normpath(join(PROJECT_ROOT, 'apps')))

DEFAULT_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken'
]

LOCAL_APPS = [
    'oauth',
    'users',
    'groups',
    'utils'
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': PROJECT_TEMPLATES,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

SECRET_FILE = normpath(join(PROJECT_ROOT, 'run', 'SECRET.key'))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': environ.get('DATABASE_NAME'),
        'USER': environ.get('DATABASE_USER'),
        'PASSWORD': environ.get('DATABASE_PASSWORD'),
        'HOST': environ.get('DATABASE_HOST'),
        'PORT': environ.get('DATABASE_PORT'),
    }
}

WSGI_APPLICATION = '%s.wsgi.application' % SITE_NAME

ROOT_URLCONF = '%s.urls' % SITE_NAME

SITE_ID = 1

STATIC_URL = '/static/'

MEDIA_URL = '/images/'

DEBUG = False

LANGUAGE_CODE = 'en-US'

TIME_ZONE = environ.get('TIME_ZONE', 'UTC')

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation'
                '.NumericPasswordValidator',
    },
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'oauth.authentication.TokenAuthentication',
    ]
}

LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s :: %(asctime)s :: '
                      '%(name)s :: %(funcName)s :: %(message)s '
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': environ.get('LOG_LEVEL')
        },
        'django': {
            'handlers': ['console'],
            'level': environ.get('LOG_LEVEL')
        },
        'oauth': {
            'handlers': ['console'],
            'level': environ.get('LOG_LEVEL')
        },
        'users': {
            'handlers': ['console'],
            'level': environ.get('LOG_LEVEL')
        },
        'groups': {
            'handlers': ['console'],
            'level': environ.get('LOG_LEVEL')
        }
    }
}

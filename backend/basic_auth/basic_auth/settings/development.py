from .common import *


ALLOWED_HOSTS = [
    '*'
]

CORS_ORIGIN_ALLOW_ALL = True

DEBUG = True

THIRD_PARTY_APPS += [
    'django_extensions',
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

INTERNAL_IPS = [
    '127.0.0.1'
]

DEBUG_TOOLBAR_CONFIG = {
    'PROFILER_MAX_DEPTH': 30,
    'SQL_WARNING_THRESHOLD': 100
}

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS

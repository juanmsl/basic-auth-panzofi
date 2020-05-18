from .common import *
from os import environ


ALLOWED_HOSTS = []

CORS_ORIGIN_WHITELIST = []

if environ.get("ALLOW_HOST") is not None:
    ALLOWED_HOSTS += [
        "{0}".format(host)
        for host in environ.get("ALLOW_HOST", "").split(", ")
    ]

if environ.get("ALLOW_NAMES") is not None:
    ALLOWED_HOSTS += [
        "{0}".format(host_name)
        for host_name in environ.get("ALLOW_NAMES", "").split(", ")
    ]

    CORS_ORIGIN_WHITELIST += [
        "{0}".format(host_name)
        for host_name in environ.get("ALLOW_NAMES", "").split(", ")
    ]

DEBUG = False

ROOT_URLCONF = '%s.%s.urls' % (SITE_NAME, SITE_NAME)

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS

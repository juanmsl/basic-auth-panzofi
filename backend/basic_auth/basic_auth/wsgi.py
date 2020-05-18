"""
WSGI config for auth project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""


import os
from .settings.common import SITE_NAME
from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    '{0}.{1}.settings.production'.format(SITE_NAME, SITE_NAME)
)

application = get_wsgi_application()

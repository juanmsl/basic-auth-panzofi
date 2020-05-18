"""
ASGI config for auth project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os
from .settings.common import SITE_NAME
from django.core.asgi import get_asgi_application

os.environ.setdefault(
    'DJANGO_SETTINGS_MODULE',
    '{0}.{1}.settings.production'.format(SITE_NAME, SITE_NAME)
)

application = get_asgi_application()

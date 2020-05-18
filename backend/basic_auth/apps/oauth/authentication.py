import logging

from django.utils.translation import ugettext as _
from rest_framework import authentication
from rest_framework import exceptions
from rest_framework.authtoken.models import Token

logger = logging.getLogger(__name__)


class TokenAuthentication(
    authentication.TokenAuthentication
):
    model = Token
    keyword = 'token'

    def authenticate(self, request):
        auth = super().authenticate(request)

        if auth is None:
            msg = _('Missing Authorization header.')
            raise exceptions.AuthenticationFailed(msg)

        return auth

    def authenticate_credentials(self, key):
        try:
            token = Token.objects.get(
                key=key
            )
        except Token.DoesNotExist:
            msg = _('Token malformed or not found.')
            raise exceptions.AuthenticationFailed(msg)

        user = token.user

        if not user.is_active:
            msg = _('User account is disabled.')
            raise exceptions.AuthenticationFailed(msg)

        return user, token

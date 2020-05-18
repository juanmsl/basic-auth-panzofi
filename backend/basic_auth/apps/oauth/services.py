from typing import Tuple

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions
from rest_framework.authtoken.models import Token

from users.models import Session


def validate_credentials(
        *,
        username: str,
        password: str
) -> Tuple[User, Token]:
    if username and password:
        user = authenticate(
            username=username,
            password=password
        )

        if user:
            if not user.is_active:
                msg = _('User account is not active.')
                raise exceptions.ValidationError(msg, code='authorization')
        else:
            msg = _('Unable to log in with provided credentials.')
            raise exceptions.ValidationError(msg, code='authorization')
    else:
        msg = _('Must include "username" and "password".')
        raise exceptions.ValidationError(msg, code='authorization')

    token = get_token(
        user=user
    )

    return user, token


def get_token(
        *,
        user: User
) -> Token:
    token, created = Token.objects.get_or_create(
        user=user
    )

    if created:
        session, created = Session.objects.get_or_create(
            user=user
        )
        if not created:
            session.delete()
            Session.objects.create(
                user=user
            )

    return token

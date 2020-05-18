import getpass
import logging

from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand
from rest_framework import exceptions
from django.utils.translation import ugettext_lazy as _

from groups import constants
from users.serializers import (
    CreateUserInputSerializer
)

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Create admin user to start using database.'

    def add_arguments(self, parser):
        parser.add_argument('--username', dest="username",
                            required=False, nargs='?', type=str)
        parser.add_argument('--password', dest="password",
                            required=False, nargs='?', type=str)
        parser.add_argument('--first-name', dest="first_name",
                            required=False, nargs='?', type=str)
        parser.add_argument('--last-name', dest="last_name",
                            required=False, nargs='?', type=str)
        parser.add_argument('--email', dest="email",
                            required=False, nargs='?', type=str)

    def handle(self, *args, **options):
        data = dict(
            username=options.get('username', None),
            password=options.get('password', None),
            first_name=options.get('first_name', None),
            last_name=options.get('last_name', None),
            email=options.get('email', None),
        )

        if data['username'] is None:
            data['username'] = 'admin'

        if data['password'] is None:
            data['password'] = 'qwerty'

        if data['first_name'] is None:
            data['first_name'] = 'admin'

        if data['last_name'] is None:
            data['last_name'] = 'user'

        if data['email'] is None:
            data['email'] = 'admin@mail.com'

        group, created = Group.objects.get_or_create(
            name=constants.GroupsConstants.ADMINISTRATOR.value
        )

        data.update(dict(
            groups=[group.id]
        ))

        try:
            input_serializer = CreateUserInputSerializer(
                data=data
            )
            input_serializer.is_valid(raise_exception=True)
            user = input_serializer.save()

            if user is not None:
                logger.info('User created')

        except exceptions.ValidationError:
            msg = _('User already exists')
            logger.error(msg)

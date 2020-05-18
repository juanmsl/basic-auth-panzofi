import logging
import names

from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext_lazy as _
from rest_framework import exceptions

from groups import constants
from users.serializers import (
    CreateUserInputSerializer
)

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Create random users to start using database.'

    def add_arguments(self, parser):
        parser.add_argument('--count', dest="count",
                            required=False, nargs='?', type=int)

    def handle(self, *args, **options):
        count = options.get('count')

        if count is None:
            count = 35

        for i in range(count):
            data = dict(
                username=f'user_{i}',
                password=f'qwerty_{i}',
                first_name=names.get_first_name(),
                last_name=names.get_last_name(),
                email=f'user_{i}@mail.com',
            )

            group, created = Group.objects.get_or_create(
                name=constants.GroupsConstants.NORMAL.value
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
                    logger.info(f'User created ({input_serializer.validated_data})')

            except exceptions.ValidationError:
                msg = _('User already exists')
                logger.error(msg)

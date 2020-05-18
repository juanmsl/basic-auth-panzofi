import logging

from django.contrib.auth.models import Group
from django.core.management.base import BaseCommand
from django.utils.translation import ugettext_lazy as _

from groups import constants

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = 'Create groups in database.'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        for groupConstants in constants.GroupsConstants:
            group, created = Group.objects.get_or_create(
                name=groupConstants.value
            )

            if created:
                msg = _(f'group {groupConstants.value} created')
            else:
                msg = _(f'group {groupConstants.value} already exists')

            logger.info(msg)

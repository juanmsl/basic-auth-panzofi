from typing import Tuple

from django.contrib.auth.models import Group, User


def add_user_to_groups(
    *,
    user: User,
    groups: Tuple[Group]
):
    for group in groups:
        add_user_to_group(
            user=user,
            group=group
        )


def add_user_to_group(
    *,
    user: User,
    group: Group
):
    user.groups.add(
        group
    )


def remove_user_from_group(
    *,
    user: User,
    group: Group
):
    user.groups.remove(
        group
    )

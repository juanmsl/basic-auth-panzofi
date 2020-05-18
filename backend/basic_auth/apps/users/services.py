from typing import Tuple

from django.contrib.auth.models import Group, User

from groups import services as group_services
from users.models import Counter
from users.constants import CounterConstant


def create_user(
        *,
        first_name: str,
        last_name: str,
        username: str,
        email: str,
        password: str,
        groups: Tuple[Group] = tuple()
) -> User:
    user = User.objects.create_user(
        first_name=first_name,
        last_name=last_name,
        username=username,
        email=email,
        password=password
    )

    group_services.add_user_to_groups(
        groups=groups,
        user=user
    )

    for counter in CounterConstant:
        Counter.objects.create(
            user=user,
            label=counter.value
        )

    return user

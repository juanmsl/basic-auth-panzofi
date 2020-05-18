from django.contrib.auth.models import Group
from rest_framework import permissions, exceptions


class GroupPermissionMixin(permissions.BasePermission):

    group = None

    def get_or_create_group(self):
        return Group.objects.get_or_create(
            name=self.group
        )

    def has_permission(self, request, view):
        if self.group is None:
            raise exceptions.ValidationError(
                f'Group must be specified in the class'
            )

        user = request.user
        group, created = self.get_or_create_group()

        user_belongs_to_group = user.groups.filter(
            id=group.id
        ).exists()

        if not user_belongs_to_group:
            raise exceptions.PermissionDenied(
                f'The user does not belong to the group {self.group}.'
            )

        return user_belongs_to_group

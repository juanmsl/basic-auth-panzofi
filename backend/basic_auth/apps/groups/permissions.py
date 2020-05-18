from groups import mixins, constants


class IsAdminPermission(mixins.GroupPermissionMixin):
    group = constants.GroupsConstants.ADMINISTRATOR.value


class IsNormalPermission(mixins.GroupPermissionMixin):
    group = constants.GroupsConstants.NORMAL.value

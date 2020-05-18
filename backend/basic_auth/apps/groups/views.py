from django.contrib.auth.models import Group
from rest_framework import permissions, generics
from rest_framework.response import Response

from groups import serializers
from groups import services
from groups import permissions as group_permissions
from oauth import authentication
from utils import views


class GroupListView(
    views.ListModelView
):
    authentication_classes = [
        authentication.TokenAuthentication
    ]
    permission_classes = [
        permissions.IsAuthenticated,
        group_permissions.IsAdminPermission
    ]

    queryset = Group.objects.all()
    OutputSerializer = serializers.GroupOutputSerializer


class GroupUserView(
    generics.GenericAPIView
):
    authentication_classes = [
        authentication.TokenAuthentication
    ]
    permission_classes = [
        permissions.IsAuthenticated,
        group_permissions.IsAdminPermission
    ]

    InputSerializer = serializers.GroupUserInputSerializer

    def post(self, request, group_id, user_id):
        data = dict(
            group_id=group_id,
            user_id=user_id
        )

        input_serializers = self.InputSerializer(
            data=data
        )
        input_serializers.is_valid(raise_exception=True)

        services.add_user_to_group(
            **input_serializers.validated_data
        )

        return Response()

    def delete(self, request, group_id, user_id):
        data = dict(
            group_id=group_id,
            user_id=user_id
        )

        input_serializers = self.InputSerializer(
            data=data
        )
        input_serializers.is_valid(raise_exception=True)

        services.remove_user_from_group(
            **input_serializers.validated_data
        )

        return Response()

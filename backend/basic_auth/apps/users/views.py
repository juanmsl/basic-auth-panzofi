from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from users.models import Counter
from utils import views
from users import serializers
from groups import permissions as group_permissions
from oauth import authentication, constants


class UserListView(
    views.ListCreateModelView
):
    authentication_classes = [
        authentication.TokenAuthentication
    ]
    permission_classes = [
        permissions.IsAuthenticated,
        group_permissions.IsAdminPermission
    ]

    queryset = User.objects.all()
    OutputSerializer = serializers.UserOutputSerializer
    InputSerializer = serializers.CreateUserInputSerializer


class UserDetailView(
    views.RetrieveUpdateDestroyModelView
):
    authentication_classes = [
        authentication.TokenAuthentication
    ]
    permission_classes = [
        permissions.IsAuthenticated,
        group_permissions.IsAdminPermission
    ]

    lookup_field = 'id'
    queryset = User.objects.all()
    OutputSerializer = serializers.UserOutputSerializer
    InputSerializer = serializers.UpdateUserInputSerializer


class CounterView(
    GenericAPIView
):
    authentication_classes = [
        authentication.TokenAuthentication
    ]
    permission_classes = [
        permissions.IsAuthenticated
    ]

    OutputSerializer = serializers.CounterOutputSerializer
    InputSerializer = serializers.UpdateCounterInputSerializer

    def put(self, request, label):
        instance = Counter.objects.get(
            label=label,
            user=request.user
        )

        input_serializer = self.InputSerializer(
            instance,
            data=request.data
        )
        input_serializer.is_valid(raise_exception=True)

        instance = input_serializer.save()

        output_serializer = self.OutputSerializer(
            instance
        )

        return Response(
            data=output_serializer.data
        )


class BasicDataView(
    GenericAPIView
):
    authentication_classes = [
        authentication.TokenAuthentication
    ]
    permission_classes = [
        permissions.IsAuthenticated
    ]

    OutputSerializer = serializers.UserOutputSerializer

    def get(self, request):
        output_serializer = self.OutputSerializer(
            request.user
        )
        data = dict(
            user=output_serializer.data,
            app_title=constants.APP.APP_NAME.value,
            app_description=constants.APP.APP_DESCRIPTION.value,
            app_logo=constants.APP.APP_LOGO_B64.value,
        )

        return Response(
            data=data
        )

from rest_framework import authentication, permissions
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from oauth import serializers
from oauth import authentication as auth_authentication


class TokenView(
    GenericAPIView
):
    authentication_classes = [
        authentication.BasicAuthentication
    ]
    permission_classes = []

    OutputSerializer = serializers.TokenOutputSerializer
    InputSerializer = serializers.TokenInputSerializer

    def post(self, request):
        serializer = self.InputSerializer(
            data=request.data
        )
        serializer.is_valid(raise_exception=True)

        output_serializer = self.OutputSerializer(
            serializer.validated_data['token']
        )

        return Response(
            data=output_serializer.data
        )


class LogoutView(
    GenericAPIView
):
    authentication_classes = [
        auth_authentication.TokenAuthentication
    ]
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def post(self, request):
        token = request.auth
        token.delete()

        user = request.user
        user.session.logout()

        return Response()

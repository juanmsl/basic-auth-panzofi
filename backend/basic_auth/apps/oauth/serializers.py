from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from oauth import services
from groups import constants as group_constants


class TokenInputSerializer(
    serializers.Serializer
):
    username = serializers.CharField(label=_("Username"))
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, data):
        user, token = services.validate_credentials(
            **data
        )

        validated_data = dict(
            **data,
            user=user,
            token=token
        )

        return validated_data


class TokenOutputSerializer(serializers.ModelSerializer):
    token = serializers.CharField(source='key')
    is_admin = serializers.SerializerMethodField()

    class Meta:
        model = Token
        fields = ('token', 'is_admin')

    def get_is_admin(self, token):
        user = token.user

        user_belongs_to_group = user.groups.filter(
            name=group_constants.GroupsConstants.ADMINISTRATOR.value
        ).exists()

        return user_belongs_to_group

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.exceptions import APIException

from users import services
from groups import constants as group_constants
from users.models import Session, Counter


class UpdateUserInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email'
        )

    def create(self, validated_data):
        raise APIException(
            'Method not allowed in serializer {}'.format(
                self.__name__
            )
        )


class CreateUserInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'password',
            'username',
            'first_name',
            'last_name',
            'email',
            'groups'
        )

    def create(self, validated_data):
        return services.create_user(
            **validated_data
        )

    def update(self, instance, validated_data):
        raise APIException(
            'Method not allowed in serializer {}'.format(
                self.__class__.__name__
            )
        )


class SessionOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ('logged_at', 'logout_at', 'duration')


class UpdateCounterInputSerializer(serializers.Serializer):

    def update(self, instance, validated_data):
        instance.increment()
        return instance


class CounterOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counter
        fields = ('label', 'value')


class UserOutputSerializer(serializers.HyperlinkedModelSerializer):
    full_name = serializers.SerializerMethodField()
    is_admin = serializers.SerializerMethodField()
    session = SessionOutputSerializer()
    counters = CounterOutputSerializer(many=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'full_name',
            'first_name',
            'last_name',
            'email',
            'is_admin',
            'session',
            'counters'
        )

    def get_full_name(self, user):
        return user.get_full_name()

    def get_is_admin(self, user):
        user_belongs_to_group = user.groups.filter(
            name=group_constants.GroupsConstants.ADMINISTRATOR.value
        ).exists()

        return user_belongs_to_group

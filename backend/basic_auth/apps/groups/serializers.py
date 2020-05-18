from django.contrib.auth.models import Group, User
from rest_framework import serializers

from utils.selectors import get_or_404


class GroupOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name')


class GroupUserInputSerializer(serializers.Serializer):
    group_id = serializers.IntegerField()
    user_id = serializers.IntegerField()

    def validate(self, data):
        group_id = data['group_id']
        user_id = data['user_id']

        user = get_or_404(
            User, id=user_id
        )

        group = get_or_404(
            Group, id=group_id
        )

        return {
            'group': group,
            'user': user
        }

from rest_framework import serializers

from users.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    '''
    Сериалайзер создаваемого пользователя
    '''
    class Meta:
        model = User
        fields = ['email', 'password']

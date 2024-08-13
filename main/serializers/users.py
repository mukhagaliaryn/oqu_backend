from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from main.models import CloneAccount

User = get_user_model()


# User
# ----------------------------------------------------------------------------------------------------------------------
class UserSerializer(UserCreateSerializer):

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'full_name', 'image', )


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('full_name', )


class UserAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('image', )


# Account
# ----------------------------------------------------------------------------------------------------------------------
class AccountSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = CloneAccount
        fields = ('id', 'user', 'birthday', 'gender', 'city', 'address', 'phone', )

from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
User = get_user_model()


# Accounts app
# --------------------------------------------------------------------------------------------------------
class UserSerializer(UserCreateSerializer):

    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'user_type', 'image', )


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', )


class UserAvatarSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('image', )


# Platforms app
# --------------------------------------------------------------------------------------------------------

# For student
class PlatformStatusStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')
        
from rest_framework import serializers
from accounts.serializers import UserSerializer
from profiles.models import Profile


class AuthorsListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'user', 'is_author', )

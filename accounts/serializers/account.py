from rest_framework import serializers
from ..models import Account
from .user import UserSerializer


# Account serializers
# --------------------------------------------------------------------------------------------------------
class AccountSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Account
        fields = ('id', 'user', 'birthday', 'gender', 'city', 'address', 'phone', )

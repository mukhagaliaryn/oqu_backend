from rest_framework import serializers

from src.platform.myaccount.models import Account
from src.platform.myaccount.serializers.users import UserSerializer


# Account
# ----------------------------------------------------------------------------------------------------------------------
class AccountSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Account
        exclude = ('specialty',  'bio', )

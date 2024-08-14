from rest_framework import views, status
from rest_framework.response import Response
from src.platform.myaccount.serializers.accounts import AccountSerializer


class MainMyAccount(views.APIView):

    def get(self, request):
        account = request.user.account
        account = AccountSerializer(account, partial=True)
        context = {
            'account': account.data
        }
        return Response(context, status=status.HTTP_200_OK)

from rest_framework.generics import views
from rest_framework import status, permissions
from rest_framework.response import Response
from .models import User
from rest_framework.parsers import MultiPartParser, FormParser

from .serializers import AccountSerializer
from .serializers import UserSerializer, UserUpdateSerializer, UserAvatarSerializer


# All myaccount
# ----------------------------------------------------------------------------------------------------------
class UsersView(views.APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):
        users = User.objects.all()
        users_serializer = UserSerializer(users, many=True)

        context = {
            'myaccount': users_serializer.data
        }
        return Response(context, status=status.HTTP_200_OK)


# Own user
# ----------------------------------------------------------------------------------------------------------
class UserAccountView(views.APIView):

    def get(self, request):
        user_account = request.user.account
        user_serializer = AccountSerializer(user_account, partial=True)

        return Response(user_serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        user = request.user
        account = user.account
        user_serializer = UserUpdateSerializer(user, data=request.data)
        account_serializer = AccountSerializer(account, data=request.data, partial=True)
        if user_serializer.is_valid() and account_serializer.is_valid():
            user_serializer.save()
            account_serializer.save()
            return Response({'success': 'Account edited successfully!'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Something wrong!'}, status=status.HTTP_400_BAD_REQUEST)


class UserAvatarAPIView(views.APIView):
    parser_classes = [MultiPartParser, FormParser, ]

    def post(self, request):
        user = request.user
        avatar_serializer = UserAvatarSerializer(user, data=request.data, partial=True, context={'request': request})
        if avatar_serializer.is_valid():
            avatar_serializer.save()
            return Response(avatar_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(avatar_serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        user = request.user
        user.image.delete()
        return Response({'deleted': True}, status=status.HTTP_204_NO_CONTENT)
    
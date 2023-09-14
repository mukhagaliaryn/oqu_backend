from django.shortcuts import get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from products.models import Category, Topic
from products.serializers import TopicSerializer, CategorySerializer
from .serializers import PlatformStatusStudentClassGroupSerializer


# Main APIView
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
class MainAPIView(APIView):

    def get(self, request):
        user_type = request.user.user_type

        if user_type == 'STUDENT':
            user = request.user
            class_group = user.classgroup_set.all().first()
            official = class_group.students.filter(id=user.id).exists()

            class_group_serializer = PlatformStatusStudentClassGroupSerializer(
                class_group, partial=True, context={'request': request}
            )
            context = {
                'official_student': official,
                'class_group': class_group_serializer.data,
            }
            return Response(context, status=status.HTTP_200_OK)
        else:
            return Response({'user_type': user_type})


# Explorer APIView
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
class ExplorerAPIView(APIView):

    def get(self, request):
        user_type = request.user.user_type

        if user_type == 'STUDENT':
            categories = get_list_or_404(Category, slug='courses')
            topics = get_list_or_404(Topic, category__slug='courses')
            categories_serializers = CategorySerializer(categories, many=True, context={'request': request})
            topics_serializers = TopicSerializer(topics, many=True, context={'request': request})
            context = {
                'user_type': request.user.user_type,
                'categories': categories_serializers.data,
                'topics': topics_serializers.data,
            }
            return Response(context, status=status.HTTP_200_OK)
        else:
            return Response({'user_type': user_type})

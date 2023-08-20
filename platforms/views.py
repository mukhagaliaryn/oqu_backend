from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from accounts.serializers.groups import PlatformStatusStudentClassGroupSerializer
from products.models import Product
from products.serializers.product import ExplorerProductSerializer, ProductSerializer


# Main view
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
                'class_group': class_group_serializer.data,
                'official_student': official
            }
            return Response(context, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Платформа не дал вам статуса учреждения.'})


# Explorer view
# ----------------------------------------------------------------------------------------
class ExplorerAPIView(APIView):

    def get(self, request):
        user_type = request.user.user_type
        if user_type == 'STUDENT':
            courses = get_list_or_404(Product, product_type='COURSE')
            courses_serializers = ExplorerProductSerializer(courses, many=True, context={'request': request})
            context = {
                'courses': courses_serializers.data
            }
            return Response(context, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Платформа не дал вам статуса учреждения.'})


# Product view
# ----------------------------------------------------------------------------------------
class ProductAPIView(APIView):

    def get(self, request, pk):
        user_type = request.user.user_type
        if user_type == 'STUDENT':
            product = get_object_or_404(Product, pk=pk)
            product_serializer = ProductSerializer(product, partial=True, context={'request': request})
            return Response(product_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Платформа не дал вам статуса учреждения.'})

from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.models import Product, Topic, Category
from products.serializers.category import TopicSerializer, CategorySerializer
from products.serializers.product import ProductSerializer


# Explorer view
# ----------------------------------------------------------------------------------------
class ExplorerAPIView(APIView):

    def get(self, request):
        categories = get_list_or_404(Category, slug='courses')
        topics = get_list_or_404(Topic, category__slug='courses')
        categories_serializers = CategorySerializer(categories, many=True, context={'request': request})
        topics_serializers = TopicSerializer(topics, many=True, context={'request': request})
        context = {
            'categories': categories_serializers.data,
            'topics': topics_serializers.data,
            'user_type': request.user.user_type
        }
        return Response(context, status=status.HTTP_200_OK)


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
            return Response({'user_type': user_type})

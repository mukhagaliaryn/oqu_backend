from rest_framework import serializers

from products.models import Product
from products.serializers.category import TopicSerializer


# Platform
class PlatformStudentProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'poster', 'class_level', )


# Explorer
class ExplorerProductSerializer(serializers.ModelSerializer):
    topic = TopicSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('name', 'poster', 'product_type', 'topic', 'authors', )


# Product
class ProductSerializer(serializers.ModelSerializer):
    topic = TopicSerializer(read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

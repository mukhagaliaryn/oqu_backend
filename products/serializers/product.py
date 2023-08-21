from rest_framework import serializers
from products.models import Product
from accounts.serializers.user import ProductUserSerializer
from products.serializers.category import TopicSerializer


# Platform view
# -----------------------------------------------------------------------------------------
class PlatformStudentProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'poster', 'class_level', )


# Explorer view
# -----------------------------------------------------------------------------------------
class ExplorerProductSerializer(serializers.ModelSerializer):
    topic = TopicSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('name', 'poster', 'product_type', 'topic', 'authors', )


# Product view
# -----------------------------------------------------------------------------------------
class ProductSerializer(serializers.ModelSerializer):
    topic = TopicSerializer(read_only=True)
    authors = ProductUserSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

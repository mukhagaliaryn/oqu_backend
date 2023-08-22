from rest_framework import serializers

from accounts.models import User
from .models import Category, Topic, Product, Chapter, Purpose, Feature, Lesson


# Generic category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', )


class TopicSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Topic
        fields = ('id', 'name', 'slug', 'category',)


# Product view
# --------------------------------------------------------------------------------------------------
class ProductAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'image', )


# Purpose
class ProductPurposeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purpose
        fields = ('id', 'item', )


# Feature
class ProductFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ('id', 'label', 'item', )


# Chapter
class ProductChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('id', 'chapter_name', )


# Lesson
class ProductLessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


# Result serializer
class ProductSerializer(serializers.ModelSerializer):
    topic = TopicSerializer(read_only=True)
    authors = ProductAuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

from rest_framework import serializers
from accounts.models import User
from products.models import Category, Topic, Purpose, Feature, Chapter, Lesson, Product


# Category
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

# Category
# -----------------------------------------------------------------------------------
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', )


# Topic
# -----------------------------------------------------------------------------------
class TopicSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Topic
        fields = ('id', 'name', 'slug', 'category',)


# Product APIView
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

# Product Detail
# -----------------------------------------------------------------------------------

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
        fields = ('id', 'title', 'chapter', 'duration', )

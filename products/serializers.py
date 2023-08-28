from rest_framework import serializers

from accounts.models import User
from .models import Category, Topic, Product, Chapter, Purpose, Feature, Lesson, Video, Task


# Generic category
# --------------------------------------------------------------------------------------------------
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


# Chapter view
# --------------------------------------------------------------------------------------------------
class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('id', 'chapter_name', 'date_created', 'about', )


# Video
class ChapterVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'lesson', 'title', )


# Tasks
class ChapterTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'lesson', 'title', 'task_type', )


# Lesson view
# --------------------------------------------------------------------------------------------------
class LessonVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class LessonTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

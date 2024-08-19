from rest_framework import serializers
from src.platform.myaccount.models import User
from src.platform.resources.models import Subcategory, Language, Purpose, Rating, Chapter, Lesson, Video, Course


class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'full_name', 'email', 'image', )


class LnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'name', 'slug', )


class SubcategoryCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ('id', 'name_en', 'name_ru', 'name_kk', 'slug', )


# Purpose
class PurposeCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purpose
        fields = ('id', 'item_kk', )


# Rating
class RatingsCourseSerializer(serializers.ModelSerializer):
    user = AuthorsSerializer(read_only=True)

    class Meta:
        model = Rating
        fields = ('id', 'user', 'assessment', 'comment', )


# Chapter
class ChaptersCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('id', 'name_en', 'name_ru', 'name_kk', 'order', )


# Lesson
class LessonsCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ('id', 'chapter', 'title_en', 'title_ru', 'title_kk', 'duration', 'order', )


# Video
class VideoListCourseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = ('id', 'url', )


# Course Detail
class CourseSerializer(serializers.ModelSerializer):
    sub_category = SubcategoryCourseSerializer(read_only=True)
    authors = AuthorsSerializer(many=True)
    ln = LnSerializer(many=True)

    class Meta:
        model = Course
        exclude = ('name', 'about', )

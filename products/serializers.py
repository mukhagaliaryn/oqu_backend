from rest_framework import serializers

from accounts.serializers import UserSerializer
from products.models import Category, Topic, Course, Language, Purpose, Rating, Lesson, Chapter, Video, Article


# Category serializers
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# Category
# ----------------------------------------------------------------------------------------------------------------------
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'name_kk', 'slug', )


# Topic
# ----------------------------------------------------------------------------------------------------------------------
class TopicSerializer(serializers.ModelSerializer):
    own = CategorySerializer(read_only=True)

    class Meta:
        model = Topic
        fields = ('id', 'name', 'name_kk', 'slug', 'own',)


# Course serializers
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

# Course lists
# ----------------------------------------------------------------------------------------------------------------------
class HeadlinerCourseListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('id', 'name', 'about', 'image', 'poster', )


class LastCourseListSerializer(serializers.ModelSerializer):
    authors = UserSerializer(many=True)

    class Meta:
        model = Course
        fields = ('id', 'name', 'image', 'course_type', 'authors', 'all_rating', )


# Course detail
# ----------------------------------------------------------------------------------------------------------------------
class LnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'name', 'slug',)


class PurposeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purpose
        fields = ('id', 'item',)


class RatingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Rating
        fields = ('id', 'user', 'rating_score', 'comment', )


# Chapter
class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('id', 'chapter_name', )


# Lessons list
class LessonListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ('id', 'chapter', 'title', 'lesson_type', 'duration', )


# Course detail
class CourseDetailSerializer(serializers.ModelSerializer):
    topic = TopicSerializer(read_only=True)
    authors = UserSerializer(many=True)
    ln = LnSerializer(many=True)

    class Meta:
        model = Course
        exclude = ('category', 'poster', 'date_created', 'is_headline', )


# Course player
# ----------------------------------------------------------------------------------------------------------------------
class LessonSerializer(serializers.ModelSerializer):
    chapter = ChapterSerializer(read_only=True)

    class Meta:
        model = Lesson
        fields = ('id', 'chapter', 'title', 'lesson_type', 'index', 'duration', )


class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'

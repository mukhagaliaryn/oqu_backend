from rest_framework import serializers

from accounts.models import User
from products.models import Language, Purpose, Rating, Chapter, Lesson, Topic, Course, Video


class AuthorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'full_name', 'email', 'image', )


class CourseTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id', 'name', 'name_kk', 'slug', )


class LnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'name', 'slug', )


# Course Purpose
class CoursePurposeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purpose
        fields = ('id', 'item', )


# Course Rating
class CourseRatingListSerializer(serializers.ModelSerializer):
    user = AuthorListSerializer(read_only=True)

    class Meta:
        model = Rating
        fields = ('id', 'user', 'rating_score', 'comment', )


# Course Chapter
class CourseChapterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('id', 'chapter_index', 'chapter_name', )


# Course Lesson
class CourseLessonListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ('id', 'chapter', 'title', 'index', 'lesson_type', 'duration', )


# Course Video
class CourseVideoListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = ('id', 'frame_url', )


# Course Detail
class CourseSerializer(serializers.ModelSerializer):
    topic = CourseTopicSerializer(read_only=True)
    authors = AuthorListSerializer(many=True)
    ln = LnSerializer(many=True)

    class Meta:
        model = Course
        exclude = ('category', 'date_created', )

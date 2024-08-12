from rest_framework import serializers
from accounts.models import User
from main.models import (
    OldLanguage, OldPurpose, OldRating, OldChapter, OldLesson,
    OldSubCategory, OldCourse, OldVideo
)


class AuthorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'full_name', 'email', 'image', )


class CourseSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OldSubCategory
        fields = ('id', 'name', 'name_kk', 'slug', )


class LnSerializer(serializers.ModelSerializer):
    class Meta:
        model = OldLanguage
        fields = ('id', 'name', 'slug', )


# Course Purpose
class CoursePurposeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OldPurpose
        fields = ('id', 'item', )


# Course Rating
class CourseRatingListSerializer(serializers.ModelSerializer):
    user = AuthorListSerializer(read_only=True)

    class Meta:
        model = OldRating
        fields = ('id', 'user', 'rating_score', 'comment', )


# Course Chapter
class CourseChapterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OldChapter
        fields = ('id', 'index', 'name', )


# Course Lesson
class CourseLessonListSerializer(serializers.ModelSerializer):

    class Meta:
        model = OldLesson
        fields = ('id', 'chapter', 'title', 'index', 'lesson_type', 'duration', )


# Course Video
class CourseVideoListSerializer(serializers.ModelSerializer):

    class Meta:
        model = OldVideo
        fields = ('id', 'frame_url', )


# Course Detail
class CourseSerializer(serializers.ModelSerializer):
    sub_category = CourseSubCategorySerializer(read_only=True)
    course_authors = AuthorListSerializer(many=True)
    ln = LnSerializer(many=True)

    class Meta:
        model = OldCourse
        exclude = ('category', 'date_created', )

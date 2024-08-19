from rest_framework import serializers
from .course import CourseSerializer
from ..models import UserCourse, UserChapter, UserLesson
from ...resources.models import Lesson, Video, Chapter


# Course Player
class PlayLessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ('id', 'chapter', 'title_en', 'title_ru', 'title_kk', 'order', 'duration', )


class PlayVideoSerializer(serializers.ModelSerializer):
    lesson = PlayLessonSerializer(read_only=True)

    class Meta:
        model = Video
        fields = '__all__'


# User Course Statistics
class PlayUserCourseSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)

    class Meta:
        model = UserCourse
        fields = ('id', 'course', 'is_completed', )


# Play Chapter List
class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('id', 'name_en', 'name_ru', 'name_kk', 'order',)


class PlayUserChapterListSerializer(serializers.ModelSerializer):
    chapter = ChapterSerializer(read_only=True)

    class Meta:
        model = UserChapter
        fields = ('id', 'chapter', 'is_completed', )


# Play Lesson List
class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ('id', 'chapter', 'title_en', 'title_ru', 'title_kk', 'duration', 'order', )


class PlayUserLessonListSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(read_only=True)

    class Meta:
        model = UserLesson
        fields = ('id', 'lesson', 'is_completed', )

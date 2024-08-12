from rest_framework import serializers
from .course import CourseSerializer
from main.models import OldLesson, OldVideo, OldArticle, OldChapter, OldUserCourse, OldUserChapter, OldUserLesson


# Course Player
class PlayLessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = OldLesson
        fields = ('id', 'chapter', 'title', 'lesson_type', 'index', 'duration', )


class PlayVideoSerializer(serializers.ModelSerializer):
    lesson = PlayLessonSerializer(read_only=True)

    class Meta:
        model = OldVideo
        fields = '__all__'


class PlayArticleSerializer(serializers.ModelSerializer):
    lesson = PlayLessonSerializer(read_only=True)

    class Meta:
        model = OldArticle
        fields = '__all__'


# User Course Statistics
class PlayUserCourseSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)

    class Meta:
        model = OldUserCourse
        fields = ('id', 'course', 'is_completed', )


# Play Chapter List
class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = OldChapter
        fields = ('id', 'index', 'name', )


class PlayUserChapterListSerializer(serializers.ModelSerializer):
    chapter = ChapterSerializer(read_only=True)

    class Meta:
        model = OldUserChapter
        fields = ('id', 'chapter', 'is_completed', )


# Play Lesson List
class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = OldLesson
        fields = ('id', 'index', 'chapter', 'title', 'lesson_type', 'duration', )


class PlayUserLessonListSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(read_only=True)

    class Meta:
        model = OldUserLesson
        fields = ('id', 'lesson', 'is_completed', )

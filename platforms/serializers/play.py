from rest_framework import serializers

from platforms.serializers.course import CourseSerializer
from products.models import Lesson, Video, Article, Course, Chapter
from profiles.models import UserCourse, UserChapter, UserLesson


# Course Player
class PlayLessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ('id', 'chapter', 'title', 'lesson_type', 'index', 'duration', )


class PlayVideoSerializer(serializers.ModelSerializer):
    lesson = PlayLessonSerializer(read_only=True)

    class Meta:
        model = Video
        fields = '__all__'


class PlayArticleSerializer(serializers.ModelSerializer):
    lesson = PlayLessonSerializer(read_only=True)

    class Meta:
        model = Article
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
        fields = ('id', 'chapter_name', )


class PlayUserChapterListSerializer(serializers.ModelSerializer):
    chapter = ChapterSerializer(read_only=True)

    class Meta:
        model = UserChapter
        fields = ('id', 'chapter', 'is_completed', )


# Play Lesson List
class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = ('id', 'chapter', 'title', 'lesson_type', 'duration', )


class PlayUserLessonListSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(read_only=True)

    class Meta:
        model = UserLesson
        fields = ('id', 'lesson', 'is_completed', )

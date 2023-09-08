from rest_framework import serializers

from products.models import Task, Question, Answer, Chapter, Lesson, Video
from profiles.models import UserQuizData, UserChapter, UserProduct, UserLesson, UserVideo


# UserProduct
# -----------------------------------------------------------------------------------
class UserProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProduct
        fields = ('id', 'is_subscribe', )


# UserChapter
# -----------------------------------------------------------------------------------

# Chapter
class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('id', 'chapter_name', 'date_created', 'about', )


# Chapter list
class ChapterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('id', 'chapter_name', )


# User chapter list
class UserChapterListSerializer(serializers.ModelSerializer):
    chapter = ChapterListSerializer(read_only=True)

    class Meta:
        model = UserChapter
        fields = ('id', 'chapter',  'is_done', )


# Main
class UserChapterSerializer(serializers.ModelSerializer):
    chapter = ChapterSerializer(read_only=True)

    class Meta:
        model = UserChapter
        fields = '__all__'


# User Lesson
# -----------------------------------------------------------------------------------
# Lesson list
class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'title', 'chapter', 'duration', )


# Main list
class UserLessonListSerializer(serializers.ModelSerializer):
    lesson = LessonListSerializer(read_only=True)

    class Meta:
        model = UserLesson
        fields = '__all__'


# UserQuizData view
# -----------------------------------------------------------------------------------
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'text', )


class UserQuestionSerializer(serializers.ModelSerializer):
    get_answers = AnswerSerializer(read_only=True, many=True)

    class Meta:
        model = Question
        fields = ('id', 'title', 'body', 'format', 'get_answers',)


class UserQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'duration', 'task_type', 'body', )


# Result
class UserQuizDataSerializer(serializers.ModelSerializer):
    quiz = UserQuizSerializer(read_only=True)
    questions = UserQuestionSerializer(read_only=True, many=True)

    class Meta:
        model = UserQuizData
        fields = '__all__'

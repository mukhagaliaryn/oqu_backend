from rest_framework import serializers

from products.models import Task, Question, Answer
from profiles.models import UserQuizData, UserChapter, UserProduct


# UserProduct
# -----------------------------------------------------------------------------------
class UserProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProduct
        fields = ('id', 'is_subscribe', )


# UserChapter
# -----------------------------------------------------------------------------------
class UserChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserChapter
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

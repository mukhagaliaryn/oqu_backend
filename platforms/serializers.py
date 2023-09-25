from rest_framework import serializers

from accounts.models import User, Institution, ClassGroup
from products.models import Product
from products.serializers import TopicSerializer
from profiles.models import (
    UserChapter, UserProduct, UserLesson, UserVideo, UserTask, UserQuizData, UserAnswer
)
from products.models import (
    Chapter, Lesson, Video, Task, Answer, Question
)


# Platform app serializers
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------


# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
# Main APIView
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
class MainInstitutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Institution
        fields = ('id', 'image', 'name', 'inst_type', 'direction', )


class MainUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', )


class MainProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'poster', 'class_level', )


#  Main ClassGroup
# -----------------------------------------------------------------------------------------
class MainClassGroupSerializer(serializers.ModelSerializer):
    teacher = MainUserSerializer(read_only=True)
    institution = MainInstitutionSerializer(read_only=True)

    class Meta:
        model = ClassGroup
        fields = ('id', 'name', 'institution', 'teacher', )


#  Main UserProducts
# -----------------------------------------------------------------------------------------
class MainUserProductsSerializer(serializers.ModelSerializer):
    product = MainProductSerializer(read_only=True)

    class Meta:
        model = UserProduct
        fields = ('id', 'product', 'score', 'max_score', )


# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
# Explorer APIView
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
class ExplorerProductSerializer(serializers.ModelSerializer):
    topic = TopicSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('name', 'poster', 'product_type', 'topic', 'authors', )


# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
# UserProduct APIView
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# UserProduct Detail
# -----------------------------------------------------------------------------------------
class ProductAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'image', )


class ProductSerializer(serializers.ModelSerializer):
    topic = TopicSerializer(read_only=True)
    authors = ProductAuthorSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class UserProductDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = UserProduct
        fields = '__all__'


# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
# UserChapter APIView
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# UserChapter List
# -----------------------------------------------------------------------------------
class ChapterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('id', 'chapter_name', )


class UserChapterListSerializer(serializers.ModelSerializer):
    chapter = ChapterListSerializer(read_only=True)

    class Meta:
        model = UserChapter
        fields = ('id', 'chapter',  'is_done', )


# UserChapter Detail
# -----------------------------------------------------------------------------------
class UserChapterProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', )


class UserChapterUserProductSerializer(serializers.ModelSerializer):
    product = UserChapterProductSerializer(read_only=True)

    class Meta:
        model = UserProduct
        fields = ('id', 'product', 'is_subscribe', 'score', )


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('id', 'chapter_name', 'about', )


class UserChapterDetailSerializer(serializers.ModelSerializer):
    chapter = ChapterSerializer(read_only=True)

    class Meta:
        model = UserChapter
        fields = '__all__'


# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
# UserLesson APIView
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# UserLesson List
# -----------------------------------------------------------------------------------
class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'title', 'chapter', 'duration', )


class UserLessonListSerializer(serializers.ModelSerializer):
    lesson = LessonListSerializer(read_only=True)

    class Meta:
        model = UserLesson
        fields = '__all__'


# UserLesson Detail
# -----------------------------------------------------------------------------------
class UserLessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserLesson
        fields = ('id', 'score', 'max_score', 'is_done', )


# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
# UserVideo APIView
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# UserVideo List
# -----------------------------------------------------------------------------------
class VideoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'lesson', 'title', )


class UserVideoListSerializer(serializers.ModelSerializer):
    video = VideoListSerializer(read_only=True)

    class Meta:
        model = UserVideo
        fields = ('id', 'video', 'is_done')


# UserVideo Detail
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'


class UserVideoSerializer(serializers.ModelSerializer):
    video = VideoSerializer(read_only=True)

    class Meta:
        model = UserVideo
        fields = '__all__'


# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
# UserTask APIView
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# UserTask List
# -----------------------------------------------------------------------------------
class TaskListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'lesson', 'title', 'task_type', )


class UserTaskListSerializer(serializers.ModelSerializer):
    task = TaskListSerializer(read_only=True)

    class Meta:
        model = UserTask
        fields = ('id', 'task', 'status', )


# UserTask Detail
# -----------------------------------------------------------------------------------
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class UserTaskSerializer(serializers.ModelSerializer):
    task = TaskSerializer(read_only=True)

    class Meta:
        model = UserTask
        fields = '__all__'


# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------
# UserQuiz APIView
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# UserQuiz List
# -----------------------------------------------------------------------------------
class QuizListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'lesson', 'title', 'task_type', )


class UserQuizListSerializer(serializers.ModelSerializer):
    quiz = QuizListSerializer(read_only=True)

    class Meta:
        model = UserQuizData
        fields = ('id', 'quiz', 'status', )


# UserQuiz Detail
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


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'duration', 'task_type', 'body', )


# UserQuiz
class UserQuizDataSerializer(serializers.ModelSerializer):
    quiz = QuizSerializer(read_only=True)

    class Meta:
        model = UserQuizData
        fields = ('id', 'quiz', 'status', 'score', 'max_score', )


# UserAnswer
class UserAnswerSerializer(serializers.ModelSerializer):
    question = UserQuestionSerializer(read_only=True)

    class Meta:
        model = UserAnswer
        fields = ('id', 'question', 'answers', )


# Result UserAnswer
# -----------------------------------------------------------------------------------
class ResultAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'text', 'correct', )


class ResultUserQuestionSerializer(serializers.ModelSerializer):
    get_answers = ResultAnswerSerializer(read_only=True, many=True)

    class Meta:
        model = Question
        fields = ('id', 'title', 'body', 'format', 'get_answers',)


class ResultUserAnswerSerializer(serializers.ModelSerializer):
    question = ResultUserQuestionSerializer(read_only=True)

    class Meta:
        model = UserAnswer
        fields = ('id', 'question', 'answers', )

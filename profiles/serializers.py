from rest_framework import serializers

from products.models import Task, Question, Answer, Chapter, Lesson, Video
from profiles.models import UserQuizData, UserChapter, UserProduct, UserLesson, UserVideo, UserTask


# Product View
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

# Product Detail
# -----------------------------------------------------------------------------------
class UserProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProduct
        fields = ('id', 'is_subscribe', )


# UserChapter View
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

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
class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('id', 'chapter_name', 'about', )


class UserChapterSerializer(serializers.ModelSerializer):
    chapter = ChapterSerializer(read_only=True)

    class Meta:
        model = UserChapter
        fields = '__all__'


# UserLesson View
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

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
        fields = ('id', 'score', 'max_score', )


# UserVideo View
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

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


# UserTask View
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

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
        fields = ('id', 'task', 'is_done', )


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


# UserQuiz View
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

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


# Result
class UserQuizDataSerializer(serializers.ModelSerializer):
    quiz = QuizSerializer(read_only=True)
    questions = UserQuestionSerializer(read_only=True, many=True)

    class Meta:
        model = UserQuizData
        fields = '__all__'

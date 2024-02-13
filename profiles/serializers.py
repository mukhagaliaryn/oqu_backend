from rest_framework import serializers
from accounts.serializers import UserSerializer
from products.serializers import CourseDetailSerializer, ChapterSerializer, LessonSerializer
from profiles.models import Profile, UserCourse, UserChapter, UserLesson


class AuthorsListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ('id', 'user', 'specialty', 'is_author', )


# CoursePlayer serializer
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------

class UserCourseSerializer(serializers.ModelSerializer):
    course = CourseDetailSerializer(read_only=True)

    class Meta:
        model = UserCourse
        fields = '__all__'


class UserChapterSerializer(serializers.ModelSerializer):
    chapter = ChapterSerializer(read_only=True)

    class Meta:
        model = UserChapter
        fields = '__all__'


class UserLessonSerializer(serializers.ModelSerializer):
    lesson = LessonSerializer(read_only=True)

    class Meta:
        model = UserLesson
        fields = '__all__'

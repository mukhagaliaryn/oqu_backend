from rest_framework import serializers

from accounts.serializers import UserSerializer
from products.models import Category, Topic, Course, Language


# Category
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

# Category
# -----------------------------------------------------------------------------------
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', )


# Topic
# -----------------------------------------------------------------------------------
class TopicSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Topic
        fields = ('id', 'name', 'name_kk', 'slug', 'category',)


# Course serializers
# -----------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------

# Course lists
# -----------------------------------------------------------------------------------
class HeadlinerCourseListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('id', 'name', 'about', 'image', 'poster', )


class LastCourseListSerializer(serializers.ModelSerializer):
    authors = UserSerializer(many=True)

    class Meta:
        model = Course
        fields = ('id', 'name', 'image', 'course_type', 'authors', 'all_rating', )


# Course detail
# -----------------------------------------------------------------------------------
class LnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('id', 'name', 'slug',)


class CourseDetailSerializer(serializers.ModelSerializer):
    topic = TopicSerializer(read_only=True)
    authors = UserSerializer(many=True)
    ln = LnSerializer(many=True)

    class Meta:
        model = Course
        exclude = ('category', 'poster', 'date_created', 'is_headline', )

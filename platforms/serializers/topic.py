from rest_framework import serializers

from accounts.models import User
from products.models import Course, Category, Topic


# Topic
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'name_kk', 'slug', )


class TopicSerializer(serializers.ModelSerializer):
    own = CategorySerializer(read_only=True)

    class Meta:
        model = Topic
        fields = ('id', 'name', 'name_kk', 'slug', 'own',)


# Topic Course List
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'full_name', )


class TopicCourseListSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Course
        fields = ('id', 'name', 'image', 'course_type', 'authors', 'all_rating', )

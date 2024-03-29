from rest_framework import serializers

from accounts.models import User, Account
from products.models import Course, Topic


# Main Headliner List
class MainHeadlinerCourseListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ('id', 'name', 'about', 'poster', )


# Main Course List
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'full_name', )


class MainCourseListSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Course
        fields = ('id', 'name', 'image', 'course_type', 'authors', 'all_rating', )


# Author List
class AuthorUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'full_name', 'image', )


class MainAuthorListSerializer(serializers.ModelSerializer):
    user = AuthorUserSerializer(read_only=True)

    class Meta:
        model = Account
        fields = ('id', 'user', 'account_type', 'specialty', )


# Main Topic List
class MainTopicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('id', 'name', 'name_kk', 'slug', )

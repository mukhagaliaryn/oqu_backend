from rest_framework import serializers

from ..models import OldCourse, OldSubCategory, CloneUser, CloneAccount


# Main Headliner List
class MainHeadlinerCourseListSerializer(serializers.ModelSerializer):

    class Meta:
        model = OldCourse
        fields = ('id', 'name', 'about', 'poster', )


# Main Course List
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CloneUser
        fields = ('id', 'full_name', )


class MainCourseListSerializer(serializers.ModelSerializer):
    course_authors = AuthorSerializer(many=True)

    class Meta:
        model = OldCourse
        fields = ('id', 'name', 'poster', 'course_type', 'course_authors', 'all_rating', )


# Author List
class AuthorUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CloneUser
        fields = ('id', 'full_name', 'image', )


class MainAuthorListSerializer(serializers.ModelSerializer):
    user = AuthorUserSerializer(read_only=True)

    class Meta:
        model = CloneAccount
        fields = ('id', 'user', 'account_type', 'specialty', )


# Main SubCategory List
class MainSubCategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = OldSubCategory
        fields = ('id', 'name', 'name_kk', 'slug', )

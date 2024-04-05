from rest_framework import serializers

from accounts.models import User
from main.models import Course, Category, SubCategory


# SubCategory
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'name_kk', 'slug', )


class SubCategorySerializer(serializers.ModelSerializer):
    own = CategorySerializer(read_only=True)

    class Meta:
        model = SubCategory
        fields = ('id', 'name', 'name_kk', 'slug', 'own',)


# SubCategory Course List
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'full_name', )


class SubCategoryCourseListSerializer(serializers.ModelSerializer):
    course_authors = AuthorSerializer(many=True)

    class Meta:
        model = Course
        fields = ('id', 'name', 'poster', 'course_type', 'course_authors', 'all_rating', )

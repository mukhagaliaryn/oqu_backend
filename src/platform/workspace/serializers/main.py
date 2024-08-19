from rest_framework import serializers

from src.platform.myaccount.models import User, Account
from src.platform.resources.models import Course, Subcategory, Category


# MainWorkspace
# ----------------------------------------------------------------------------------------------------------------------

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'full_name', )


class LastCoursesMainWorkspaceSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)

    class Meta:
        model = Course
        fields = ('id', 'name_en', 'name_ru', 'name_kk', 'poster', 'course_type', 'authors', 'rating', )


# Authors
class AuthorUserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'full_name', 'image', )


class AuthorsMainWorkspaceSerializer(serializers.ModelSerializer):
    user = AuthorUserListSerializer(read_only=True)

    class Meta:
        model = Account
        fields = ('id', 'user', 'account_type', 'specialty_kk', )


# Subcategories
class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name_en', 'name_ru', 'name_kk', 'slug', )


class SubcategoriesSerializer(serializers.ModelSerializer):
    own = CategoriesSerializer(read_only=True)

    class Meta:
        model = Subcategory
        fields = ('id', 'name_en', 'name_ru', 'name_kk', 'own', 'slug', )

from rest_framework import serializers

from products.models import Category, Topic, Course
from profiles.serializers import AuthorsListSerializer


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
class LastCourseListSerializer(serializers.ModelSerializer):
    authors = AuthorsListSerializer(many=True)

    class Meta:
        model = Course
        fields = ('id', 'name', 'poster', 'course_type', 'authors', 'all_rating', )

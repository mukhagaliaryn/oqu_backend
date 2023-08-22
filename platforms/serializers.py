from rest_framework import serializers

from accounts.models import User, Institution, ClassGroup
from products.models import Product
from products.serializers import TopicSerializer


# Platform view
# -----------------------------------------------------------------------------------------
class PlatformStatusStudentInstitutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Institution
        fields = ('id', 'name', 'school_view', )


class PlatformStatusStudentUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', )


class PlatformStudentProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'poster', 'class_level', )


# Result serializer
class PlatformStatusStudentClassGroupSerializer(serializers.ModelSerializer):
    teacher = PlatformStatusStudentUserSerializer(read_only=True)
    institution = PlatformStatusStudentInstitutionSerializer(read_only=True)
    subjects = PlatformStudentProductsSerializer(many=True, read_only=True)

    class Meta:
        model = ClassGroup
        fields = ('id', 'name', 'institution', 'teacher', 'subjects')


# Explorer view
# -----------------------------------------------------------------------------------------
# Result serializer
class ExplorerProductSerializer(serializers.ModelSerializer):
    topic = TopicSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('name', 'poster', 'product_type', 'topic', 'authors', )


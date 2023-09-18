from rest_framework import serializers
from accounts.models import User, Institution, ClassGroup
from products.models import Product
from products.serializers import TopicSerializer
from profiles.models import UserProduct


# Platform APIView
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

class PlatformStatusStudentInstitutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Institution
        fields = ('id', 'name', 'school_view', )


class PlatformStatusStudentUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', )


class PlatformStudentProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'poster', 'class_level', )


class PlatformStatusStudentClassGroupSerializer(serializers.ModelSerializer):
    teacher = PlatformStatusStudentUserSerializer(read_only=True)
    institution = PlatformStatusStudentInstitutionSerializer(read_only=True)

    class Meta:
        model = ClassGroup
        fields = ('id', 'name', 'institution', 'teacher', )


class PlatformUserProductSerializer(serializers.ModelSerializer):
    product = PlatformStudentProductSerializer(read_only=True)

    class Meta:
        model = UserProduct
        fields = ('id', 'product', 'score', 'max_score', )


# Explorer view
# -----------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------

# Result serializer
class ExplorerProductSerializer(serializers.ModelSerializer):
    topic = TopicSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('name', 'poster', 'product_type', 'topic', 'authors', )


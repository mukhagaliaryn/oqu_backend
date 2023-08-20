from rest_framework import serializers
from accounts.models import ClassGroup
from accounts.serializers.institution import PlatformStudentStatusInstitutionSerializer
from accounts.serializers.user import PlatformStatusStudentSerializer
from products.serializers.product import PlatformStudentProductSerializer


# Platform
# --------------------------------------------------------------------------------------------------------
# For students
class PlatformStatusStudentClassGroupSerializer(serializers.ModelSerializer):
    teacher = PlatformStatusStudentSerializer(read_only=True)
    institution = PlatformStudentStatusInstitutionSerializer(read_only=True)
    subjects = PlatformStudentProductSerializer(many=True, read_only=True)

    class Meta:
        model = ClassGroup
        fields = ('id', 'name', 'institution', 'teacher', 'subjects')

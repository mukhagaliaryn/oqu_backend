from rest_framework import serializers
from accounts.models import Institution


# Platform
# For students
class PlatformStudentStatusInstitutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Institution
        fields = ('id', 'name', 'school_view', )

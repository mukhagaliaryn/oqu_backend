from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from accounts.serializers.groups import PlatformStatusStudentClassGroupSerializer



# Main view
# ----------------------------------------------------------------------------------------
class MainAPIView(APIView):

    def get(self, request):
        user_type = request.user.user_type

        if user_type == 'STUDENT':
            user = request.user
            class_group = user.classgroup_set.all().first()
            official = class_group.students.filter(id=user.id).exists()
            class_group_serializer = PlatformStatusStudentClassGroupSerializer(
                class_group, partial=True, context={'request': request}
            )
            context = {
                'class_group': class_group_serializer.data,
                'official_student': official
            }
            return Response(context, status=status.HTTP_200_OK)
        else:
            return Response({'user_type': user_type})

from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import Account
from main.serializers.main import MainCourseListSerializer, MainAuthorListSerializer, MainTopicListSerializer
from products.models import Course, Topic


# Main API View
# ----------------------------------------------------------------------------------------------------------------------
class MainAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):
        last_courses = Course.objects.all()[:8]
        popular_topics = Topic.objects.all()[:5]
        authors = Account.objects.filter(account_type='AUTHOR')[:8]

        last_courses_data = MainCourseListSerializer(last_courses, many=True, context={'request': request})
        authors_data = MainAuthorListSerializer(authors, many=True, context={'request': request})
        popular_topics_data = MainTopicListSerializer(popular_topics, many=True)

        context = {
            'last_courses': last_courses_data.data,
            'authors': authors_data.data,
            'popular_topics': popular_topics_data.data,
        }

        if request.user.is_authenticated:
            context['user'] = request.user.full_name

        return Response(context, status=status.HTTP_200_OK)

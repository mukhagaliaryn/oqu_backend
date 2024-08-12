from django.shortcuts import get_object_or_404
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import OldAccount
from main.models import OldCourse, OldSubCategory
from main.serializers.main import MainCourseListSerializer, MainAuthorListSerializer, MainSubCategoryListSerializer
from main.serializers.topic import SubCategorySerializer, SubCategoryCourseListSerializer


# Main API View
# ----------------------------------------------------------------------------------------------------------------------
class MainAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):
        last_courses = OldCourse.objects.all()[:8]
        popular_topics = OldSubCategory.objects.all()[:5]
        authors = OldAccount.objects.filter(account_type='AUTHOR')[:8]

        last_courses_data = MainCourseListSerializer(last_courses, many=True, context={'request': request})
        authors_data = MainAuthorListSerializer(authors, many=True, context={'request': request})
        popular_topics_data = MainSubCategoryListSerializer(popular_topics, many=True)

        context = {
            'last_courses': last_courses_data.data,
            'authors': authors_data.data,
            'popular_topics': popular_topics_data.data,
        }

        if request.user.is_authenticated:
            context['user'] = request.user.full_name

        return Response(context, status=status.HTTP_200_OK)


# Last courses
# ----------------------------------------------------------------------------------------------------------------------
class LastCoursesAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):
        last_courses = OldCourse.objects.all()[:48]
        last_courses_data = MainCourseListSerializer(last_courses, many=True, context={'request': request})
        context = {
            'last_courses': last_courses_data.data,
        }
        return Response(context, status=status.HTTP_200_OK)


# Last authors
# ----------------------------------------------------------------------------------------------------------------------
class AuthorsAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):
        authors = OldAccount.objects.filter(account_type='AUTHOR')
        authors_data = MainAuthorListSerializer(authors, many=True, context={'request': request})
        context = {
            'authors': authors_data.data,
        }
        return Response(context, status=status.HTTP_200_OK)


# Topic
# ----------------------------------------------------------------------------------------------------------------------
class TopicAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request, slug):
        sub_category = get_object_or_404(OldSubCategory, slug=slug)
        sub_category_courses = OldCourse.objects.filter(sub_category=sub_category)

        topic_data = SubCategorySerializer(sub_category, partial=True, context={'request': request})
        topic_courses_data = SubCategoryCourseListSerializer(sub_category_courses, many=True, context={'request': request})

        context = {
            'topic': topic_data.data,
            'topic_courses': topic_courses_data.data,
        }
        return Response(context, status=status.HTTP_200_OK)


# Settings
# ----------------------------------------------------------------------------------------------------------------------
class SettingsAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):

        return Response({'page': 'Settings page'}, status=status.HTTP_200_OK)
    
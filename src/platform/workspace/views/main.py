from django.shortcuts import get_object_or_404
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from src.platform.myaccount.models import Account
from src.platform.resources.models import Course, Subcategory
from src.platform.workspace.serializers.main import LastCoursesMainWorkspaceSerializer, AuthorsMainWorkspaceSerializer, \
    SubcategoriesSerializer


# MainWorkspace API
# ----------------------------------------------------------------------------------------------------------------------
class MainWorkspaceAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):
        last_courses = Course.objects.all()[:8]
        popular_topics = Subcategory.objects.all()[:5]
        authors = Account.objects.filter(account_type='AUTHOR')[:8]

        last_courses = LastCoursesMainWorkspaceSerializer(last_courses, many=True, context={'request': request})
        authors = AuthorsMainWorkspaceSerializer(authors, many=True, context={'request': request})
        popular_topics = SubcategoriesSerializer(popular_topics, many=True)

        context = {
            'last_courses': last_courses.data,
            'authors': authors.data,
            'popular_topics': popular_topics.data,
        }

        if request.user.is_authenticated:
            context['user'] = request.user.full_name

        return Response(context, status=status.HTTP_200_OK)


# LastCoursesWorkspace API
# ----------------------------------------------------------------------------------------------------------------------
class LastCoursesWorkspaceAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):
        last_courses = Course.objects.all()[:48]
        last_courses = LastCoursesMainWorkspaceSerializer(last_courses, many=True, context={'request': request})
        context = {
            'last_courses': last_courses.data,
        }
        return Response(context, status=status.HTTP_200_OK)


#  AuthorsWorkspace API
# ----------------------------------------------------------------------------------------------------------------------
class AuthorsWorkspaceAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):
        authors = Account.objects.filter(account_type='AUTHOR')
        authors = AuthorsMainWorkspaceSerializer(authors, many=True, context={'request': request})
        context = {
            'authors': authors.data,
        }
        return Response(context, status=status.HTTP_200_OK)


# SubcategoryWorkspace API
# ----------------------------------------------------------------------------------------------------------------------
class SubcategoryWorkspaceAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request, slug):
        sub_category = get_object_or_404(Subcategory, slug=slug)
        courses = Course.objects.filter(sub_category=sub_category)

        sub_category = SubcategoriesSerializer(sub_category, partial=True, context={'request': request})
        sub_category_courses = LastCoursesMainWorkspaceSerializer(courses, many=True, context={'request': request})

        context = {
            'sub_category': sub_category.data,
            'sub_category_courses': sub_category_courses.data,
        }
        return Response(context, status=status.HTTP_200_OK)


# Settings
# ----------------------------------------------------------------------------------------------------------------------
class SettingsWorkspaceAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):

        return Response({'page': 'Settings page'}, status=status.HTTP_200_OK)

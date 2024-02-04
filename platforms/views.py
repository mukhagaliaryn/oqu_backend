from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from profiles.models import Profile
from products.models import Course, Topic, Lesson
from products.serializers import (LastCourseListSerializer, HeadlinerCourseListSerializer,
                                  TopicSerializer, CourseDetailSerializer, PurposeSerializer, LessonListSerializer,
                                  ChapterSerializer)
from profiles.serializers import AuthorsListSerializer


# Main API View
# ----------------------------------------------------------------------------------------
class MainAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):
        headliners = Course.objects.filter(is_headline=True)
        last_courses = Course.objects.all()[:8]
        popular_topics = Topic.objects.all()[:4]
        authors = Profile.objects.filter(is_author=True)[:8]

        headliners_data = HeadlinerCourseListSerializer(headliners, many=True, context={'request': request})
        last_courses_data = LastCourseListSerializer(last_courses, many=True, context={'request': request})
        authors_data = AuthorsListSerializer(authors, many=True, context={'request': request})
        popular_topics_data = TopicSerializer(popular_topics, many=True)

        context = {
            'headliners': headliners_data.data,
            'last_courses': last_courses_data.data,
            'authors': authors_data.data,
            'popular_topics': popular_topics_data.data,
        }

        if request.user.is_authenticated:
            pass

        return Response(context, status=status.HTTP_200_OK)


# Last courses
class LastCoursesAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):
        last_courses = Course.objects.all()[:48]
        last_courses_data = LastCourseListSerializer(last_courses, many=True, context={'request': request})
        context = {
            'last_courses': last_courses_data.data,
        }
        return Response(context, status=status.HTTP_200_OK)


# Last courses
class AuthorsAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):
        authors = Profile.objects.filter(is_author=True)[:8]
        authors_data = AuthorsListSerializer(authors, many=True, context={'request': request})
        context = {
            'authors': authors_data.data,
        }
        return Response(context, status=status.HTTP_200_OK)


# Topics
# ----------------------------------------------------------------------------------------
class TopicAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request, slug):
        topic = get_object_or_404(Topic, slug=slug)
        topic_courses = Course.objects.filter(topic=topic)

        topic_data = TopicSerializer(topic, partial=True, context={'request': request})
        topic_courses_data = LastCourseListSerializer(topic_courses, many=True, context={'request': request})

        context = {
            'topic': topic_data.data,
            'topic_courses': topic_courses_data.data,
        }
        return Response(context, status=status.HTTP_200_OK)


# CourseDetail API View
# ----------------------------------------------------------------------------------------
class CourseDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        purposes = course.purpose_set.all()
        chapters = course.chapter_set.all()
        lessons = Lesson.objects.filter(chapter__in=chapters)

        course_data = CourseDetailSerializer(course, partial=True, context={'request': request})
        purposes_data = PurposeSerializer(purposes, many=True)
        chapters_data = ChapterSerializer(chapters, many=True)
        lessons_data = LessonListSerializer(lessons, many=True)

        context = {
            'course': course_data.data,
            'purposes': purposes_data.data,
            'chapters': chapters_data.data,
            'lessons': lessons_data.data
        }
        return Response(context, status=status.HTTP_200_OK)


# Settings
class SettingsAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):

        return Response({'page': 'Settings page'}, status=status.HTTP_200_OK)
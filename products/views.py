from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.models import Product, Lesson, Video, Task, Chapter
from profiles.models import UserQuizData, UserProduct, UserChapter, UserLesson
from profiles.serializers import UserQuizDataSerializer, UserChapterSerializer, UserChapterListSerializer, \
    UserLessonListSerializer

from .serializers import (
    ProductSerializer, ProductChapterSerializer,
    ProductPurposeSerializer, ProductFeatureSerializer,
    ProductLessonSerializer,
    ChapterVideoSerializer, ChapterTaskSerializer,
    LessonVideoSerializer, LessonTaskSerializer
)


# Product view
# ----------------------------------------------------------------------------------------
class ProductAPIView(APIView):

    def get(self, request, pk):
        user_type = request.user.user_type
        if user_type == 'STUDENT':
            product = get_object_or_404(Product, pk=pk)
            user_product = get_object_or_404(UserProduct, product=product)
            purposes = product.purpose_set.all()
            features = product.feature_set.all()
            chapters = product.chapter_set.all()
            lessons = Lesson.objects.filter(chapter__in=chapters)

            product_serializer = ProductSerializer(product, partial=True, context={'request': request})
            purposes_serializer = ProductPurposeSerializer(purposes, many=True)
            features_serializer = ProductFeatureSerializer(features, many=True)
            chapters_serializer = ProductChapterSerializer(chapters, many=True)
            lessons_serializer = ProductLessonSerializer(lessons, many=True)

            context = {
                'user_type': user_type,
                'user_product': user_product.is_subscribe,
                'product': product_serializer.data,
                'purposes': purposes_serializer.data,
                'features': features_serializer.data,
                'chapters': chapters_serializer.data,
                'lessons': lessons_serializer.data
            }
            return Response(context, status=status.HTTP_200_OK)
        else:
            return Response({'user_type': user_type})


# Chapter view
# ----------------------------------------------------------------------------------------
class ChapterAPIView(APIView):
    def get(self, request, pk, chapter_pk):
        user_type = request.user.user_type
        if user_type == 'STUDENT':
            # user chapter data
            product = get_object_or_404(Product, pk=pk)
            chapter = get_object_or_404(Chapter, pk=chapter_pk)
            user_chapter = get_object_or_404(UserChapter, chapter=chapter)

            # sidebar menu
            user_chapters = UserChapter.objects.filter(chapter__product=product)
            user_lessons = UserLesson.objects.filter(lesson__chapter=chapter)
            lessons = Lesson.objects.filter(chapter=chapter)

            # chapters list data
            videos = Video.objects.filter(lesson__in=lessons)
            tasks = Task.objects.filter(lesson__in=lessons, task_type='WRITE')
            quizzes = Task.objects.filter(lesson__in=lessons, task_type='QUIZ')

            # serializers
            user_chapter_serializer = UserChapterSerializer(user_chapter, partial=True)
            user_chapters_serializer = UserChapterListSerializer(user_chapters, many=True)
            user_lessons_serializer = UserLessonListSerializer(user_lessons, many=True)

            videos_serializers = ChapterVideoSerializer(videos, many=True)
            tasks_serializers = ChapterTaskSerializer(tasks, many=True)
            quizzes_serializers = ChapterTaskSerializer(quizzes, many=True)

            context = {
                'user_type': user_type,
                'user_chapter': user_chapter_serializer.data,
                'product': product.name,
                'user_chapters': user_chapters_serializer.data,
                'user_lessons': user_lessons_serializer.data,

                'videos': videos_serializers.data,
                'tasks': tasks_serializers.data,
                'quizzes': quizzes_serializers.data,
            }
            return Response(context, status=status.HTTP_200_OK)
        else:
            return Response({'user_type': user_type})


# Lesson view
# ----------------------------------------------------------------------------------------
# Video
class LessonVideoAPIView(APIView):
    def get(self, request, pk, chapter_pk, lesson_id, video_id):
        user_type = request.user.user_type
        if user_type == 'STUDENT':
            product = get_object_or_404(Product, pk=pk)
            chapter = get_object_or_404(Chapter, pk=chapter_pk)
            lesson = get_object_or_404(Lesson, pk=lesson_id)
            video = get_object_or_404(Video, pk=video_id)

            videos = Video.objects.filter(lesson=lesson)
            tasks = Task.objects.filter(lesson=lesson, task_type='WRITE')
            quizzes = Task.objects.filter(lesson=lesson, task_type='QUIZ')

            chapter_serializer = ProductChapterSerializer(chapter, partial=True)
            video_serializer = LessonVideoSerializer(video, partial=True, context={'request': request})

            videos_serializers = ChapterVideoSerializer(videos, many=True)
            tasks_serializers = ChapterTaskSerializer(tasks, many=True)
            quizzes_serializers = ChapterTaskSerializer(quizzes, many=True)

            context = {
                'user_type': user_type,
                'chapter': chapter_serializer.data,
                'video': video_serializer.data,

                'videos': videos_serializers.data,
                'tasks': tasks_serializers.data,
                'quizzes': quizzes_serializers.data,
            }
            return Response(context, status=status.HTTP_200_OK)
        else:
            return Response({'user_type': user_type})


# Task
class LessonTaskAPIView(APIView):
    def get(self, request, pk, chapter_pk, lesson_id, task_id):
        user_type = request.user.user_type
        if user_type == 'STUDENT':
            product = get_object_or_404(Product, pk=pk)
            chapter = get_object_or_404(Chapter, pk=chapter_pk)
            lesson = get_object_or_404(Lesson, pk=lesson_id)
            task = get_object_or_404(Task, pk=task_id, task_type='WRITE')

            videos = Video.objects.filter(lesson=lesson)
            tasks = Task.objects.filter(lesson=lesson, task_type='WRITE')
            quizzes = Task.objects.filter(lesson=lesson, task_type='QUIZ')

            chapter_serializer = ProductChapterSerializer(chapter, partial=True)
            task_serializer = LessonTaskSerializer(task, partial=True, context={'request': request})

            videos_serializers = ChapterVideoSerializer(videos, many=True)
            tasks_serializers = ChapterTaskSerializer(tasks, many=True)
            quizzes_serializers = ChapterTaskSerializer(quizzes, many=True)

            context = {
                'user_type': user_type,
                'product': product.name,
                'chapter': chapter_serializer.data,
                'task': task_serializer.data,

                'videos': videos_serializers.data,
                'tasks': tasks_serializers.data,
                'quizzes': quizzes_serializers.data,
            }
            return Response(context, status=status.HTTP_200_OK)
        else:
            return Response({'user_type': user_type})


# Quiz
class LessonQuizAPIView(APIView):
    def get(self, request, pk, chapter_pk, lesson_id, quiz_id):
        user_type = request.user.user_type
        if user_type == 'STUDENT':
            product = get_object_or_404(Product, pk=pk)
            chapter = get_object_or_404(Chapter, pk=chapter_pk)
            lesson = get_object_or_404(Lesson, pk=lesson_id)

            # user quiz data
            user_quiz_data = get_object_or_404(UserQuizData, pk=quiz_id)

            # Sidebar menu
            videos = Video.objects.filter(lesson=lesson)
            tasks = Task.objects.filter(lesson=lesson, task_type='WRITE')
            quizzes = Task.objects.filter(lesson=lesson, task_type='QUIZ')

            # serializers
            chapter_serializer = ProductChapterSerializer(chapter, partial=True)
            user_quiz_data_serializer = UserQuizDataSerializer(user_quiz_data, partial=True)
            videos_serializers = ChapterVideoSerializer(videos, many=True)
            tasks_serializers = ChapterTaskSerializer(tasks, many=True)
            quizzes_serializers = ChapterTaskSerializer(quizzes, many=True)

            context = {
                'user_type': user_type,
                'product': product.name,
                'chapter': chapter_serializer.data,
                'user_quiz_data': user_quiz_data_serializer.data,

                'videos': videos_serializers.data,
                'tasks': tasks_serializers.data,
                'quizzes': quizzes_serializers.data,
            }
            return Response(context, status=status.HTTP_200_OK)
        else:
            return Response({'user_type': user_type})




from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from products.models import Product, Lesson, Video, Task, Chapter

from .serializers import (
    ProductSerializer, ProductChapterSerializer,
    ProductPurposeSerializer, ProductFeatureSerializer,
    ProductLessonSerializer,
    ChapterSerializer, ChapterVideoSerializer, ChapterTaskSerializer,
    LessonVideoSerializer, LessonTaskSerializer
)


# Product view
# ----------------------------------------------------------------------------------------
class ProductAPIView(APIView):

    def get(self, request, pk):
        user_type = request.user.user_type
        if user_type == 'STUDENT':
            product = get_object_or_404(Product, pk=pk)
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
            product = get_object_or_404(Product, pk=pk)
            chapters = product.chapter_set.all()
            chapter = product.chapter_set.get(pk=chapter_pk)
            lessons = Lesson.objects.filter(chapter=chapter)

            videos = Video.objects.filter(lesson__in=lessons)
            tasks = Task.objects.filter(lesson__in=lessons, task_type='WRITE')
            quizzes = Task.objects.filter(lesson__in=lessons, task_type='QUIZ')

            chapter_serializer = ChapterSerializer(chapter, partial=True)
            chapters_serializer = ProductChapterSerializer(chapters, many=True)
            lessons_serializer = ProductLessonSerializer(lessons, many=True)

            videos_serializers = ChapterVideoSerializer(videos, many=True)
            tasks_serializers = ChapterTaskSerializer(tasks, many=True)
            quizzes_serializers = ChapterTaskSerializer(quizzes, many=True)

            context = {
                'user_type': user_type,
                'chapter': chapter_serializer.data,
                'product': product.name,
                'chapters': chapters_serializer.data,
                'lessons': lessons_serializer.data,

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
            quiz = get_object_or_404(Task, pk=quiz_id, task_type='QUIZ')

            videos = Video.objects.filter(lesson=lesson)
            tasks = Task.objects.filter(lesson=lesson, task_type='WRITE')
            quizzes = Task.objects.filter(lesson=lesson, task_type='QUIZ')

            chapter_serializer = ProductChapterSerializer(chapter, partial=True)
            quiz_serializer = LessonTaskSerializer(quiz, partial=True, context={'request': request})

            videos_serializers = ChapterVideoSerializer(videos, many=True)
            tasks_serializers = ChapterTaskSerializer(tasks, many=True)
            quizzes_serializers = ChapterTaskSerializer(quizzes, many=True)

            context = {
                'user_type': user_type,
                'chapter': chapter_serializer.data,
                'quiz': quiz_serializer.data,

                'videos': videos_serializers.data,
                'tasks': tasks_serializers.data,
                'quizzes': quizzes_serializers.data,
            }
            return Response(context, status=status.HTTP_200_OK)
        else:
            return Response({'user_type': user_type})

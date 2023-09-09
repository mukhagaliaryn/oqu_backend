from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from products.models import Product, Lesson, Video, Task, Chapter
from profiles.models import UserQuizData, UserProduct, UserChapter, UserLesson, UserVideo, UserTask
from profiles.serializers import (
    UserChapterSerializer, UserChapterListSerializer,
    UserLessonListSerializer, UserVideoListSerializer, UserTaskListSerializer, UserQuizListSerializer,
    UserQuizDataSerializer, UserVideoSerializer, UserTaskSerializer, UserLessonSerializer
)

from .serializers import (
    ProductSerializer, ProductChapterSerializer, ProductPurposeSerializer, ProductFeatureSerializer,
    ProductLessonSerializer,
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

            # chapters list data
            user_videos = UserVideo.objects.filter(video__lesson__chapter=chapter)
            user_tasks = UserTask.objects.filter(task__lesson__chapter=chapter)
            user_quizzes = UserQuizData.objects.filter(quiz__lesson__chapter=chapter)

            # serializers
            user_chapter_serializer = UserChapterSerializer(user_chapter, partial=True)
            user_chapters_serializer = UserChapterListSerializer(user_chapters, many=True)
            user_lessons_serializer = UserLessonListSerializer(user_lessons, many=True)

            user_videos_serializers = UserVideoListSerializer(user_videos, many=True)
            user_tasks_serializers = UserTaskListSerializer(user_tasks, many=True)
            user_quizzes_serializers = UserQuizListSerializer(user_quizzes, many=True)

            context = {
                'user_type': user_type,
                'user_chapter': user_chapter_serializer.data,
                'product': product.name,
                'user_chapters': user_chapters_serializer.data,
                'user_lessons': user_lessons_serializer.data,

                'videos': user_videos_serializers.data,
                'tasks': user_tasks_serializers.data,
                'quizzes': user_quizzes_serializers.data,
            }
            return Response(context, status=status.HTTP_200_OK)
        else:
            return Response({'user_type': user_type})


# Lesson view
# ----------------------------------------------------------------------------------------
# Video
class LessonVideoAPIView(APIView):
    def get(self, request, pk, chapter_pk, lesson_pk, video_pk):
        user_type = request.user.user_type
        if user_type == 'STUDENT':
            product = get_object_or_404(Product, pk=pk)
            chapter = get_object_or_404(Chapter, pk=chapter_pk)
            user_lesson = get_object_or_404(UserLesson, lesson__pk=lesson_pk)
            user_video = get_object_or_404(UserVideo, video__pk=video_pk)

            user_videos = UserVideo.objects.filter(video__lesson=user_lesson.lesson)
            user_tasks = UserTask.objects.filter(task__lesson=user_lesson.lesson)
            user_quizzes = UserQuizData.objects.filter(quiz__lesson=user_lesson.lesson)

            chapter_serializer = ProductChapterSerializer(chapter, partial=True)
            user_lesson_serializer = UserLessonSerializer(user_lesson, partial=True)
            user_video_serializer = UserVideoSerializer(user_video, partial=True, context={'request': request})

            user_videos_serializers = UserVideoListSerializer(user_videos, many=True)
            user_tasks_serializers = UserTaskListSerializer(user_tasks, many=True)
            user_quizzes_serializers = UserQuizListSerializer(user_quizzes, many=True)

            context = {
                'user_type': user_type,
                'product': product.name,
                'chapter': chapter_serializer.data,
                'user_lesson': user_lesson_serializer.data,
                'user_video': user_video_serializer.data,

                'videos': user_videos_serializers.data,
                'tasks': user_tasks_serializers.data,
                'quizzes': user_quizzes_serializers.data,
            }
            return Response(context, status=status.HTTP_200_OK)
        else:
            return Response({'user_type': user_type})

    def put(self, request, pk, chapter_pk, lesson_pk, video_pk):
        user_type = request.user.user_type
        if user_type == 'STUDENT':
            user_video = get_object_or_404(UserVideo, video__pk=video_pk)

            # user video sum
            user_video.score += 20
            user_video.is_done = True
            user_video.save()
            return Response({'status': 'All OK'})
        else:
            return Response({'user_type': user_type})


# Task
class LessonTaskAPIView(APIView):
    def get(self, request, pk, chapter_pk, lesson_pk, task_pk):
        user_type = request.user.user_type
        if user_type == 'STUDENT':
            product = get_object_or_404(Product, pk=pk)
            chapter = get_object_or_404(Chapter, pk=chapter_pk)
            lesson = get_object_or_404(Lesson, pk=lesson_pk)
            task = get_object_or_404(Task, pk=task_pk, task_type='WRITE')
            user_task = get_object_or_404(UserTask, task=task)

            user_videos = UserVideo.objects.filter(video__lesson=lesson)
            user_tasks = UserTask.objects.filter(task__lesson=lesson)
            user_quizzes = UserQuizData.objects.filter(quiz__lesson=lesson)

            chapter_serializer = ProductChapterSerializer(chapter, partial=True)
            user_task_serializer = UserTaskSerializer(user_task, partial=True, context={'request': request})

            user_videos_serializers = UserVideoListSerializer(user_videos, many=True)
            user_tasks_serializers = UserTaskListSerializer(user_tasks, many=True)
            user_quizzes_serializers = UserQuizListSerializer(user_quizzes, many=True)

            context = {
                'user_type': user_type,
                'product': product.name,
                'chapter': chapter_serializer.data,
                'user_task': user_task_serializer.data,

                'videos': user_videos_serializers.data,
                'tasks': user_tasks_serializers.data,
                'quizzes': user_quizzes_serializers.data,
            }
            return Response(context, status=status.HTTP_200_OK)
        else:
            return Response({'user_type': user_type})

    def put(self, request, pk, chapter_pk, lesson_id, task_pk):
        user_type = request.user.user_type
        if user_type == 'STUDENT':
            user_task = get_object_or_404(UserTask, task__pk=task_pk)
            user_task.score += 30
            user_task.is_done = True
            user_task.save()
            return Response({'status': 'All OK'})
        else:
            return Response({'user_type': user_type})


# Quiz
class LessonQuizAPIView(APIView):
    def get(self, request, pk, chapter_pk, lesson_pk, quiz_pk):
        user_type = request.user.user_type
        if user_type == 'STUDENT':
            product = get_object_or_404(Product, pk=pk)
            chapter = get_object_or_404(Chapter, pk=chapter_pk)
            lesson = get_object_or_404(Lesson, pk=lesson_pk)

            # user quiz data
            user_quiz_data = get_object_or_404(UserQuizData, quiz=quiz_pk)

            # Sidebar menu
            user_videos = UserVideo.objects.filter(video__lesson=lesson)
            user_tasks = UserTask.objects.filter(task__lesson=lesson)
            user_quizzes = UserQuizData.objects.filter(quiz__lesson=lesson)

            # serializers
            user_quiz_data_serializer = UserQuizDataSerializer(user_quiz_data, partial=True)
            chapter_serializer = ProductChapterSerializer(chapter, partial=True)
            user_videos_serializers = UserVideoListSerializer(user_videos, many=True)
            user_tasks_serializers = UserTaskListSerializer(user_tasks, many=True)
            user_quizzes_serializers = UserQuizListSerializer(user_quizzes, many=True)

            context = {
                'user_type': user_type,
                'product': product.name,
                'chapter': chapter_serializer.data,
                'user_quiz_data': user_quiz_data_serializer.data,

                'videos': user_videos_serializers.data,
                'tasks': user_tasks_serializers.data,
                'quizzes': user_quizzes_serializers.data,
            }
            return Response(context, status=status.HTTP_200_OK)
        else:
            return Response({'user_type': user_type})

    def put(self, request, pk, chapter_pk, lesson_pk, quiz_pk):
        user_type = request.user.user_type
        if user_type == 'STUDENT':
            user_quiz = get_object_or_404(UserQuizData, quiz__pk=quiz_pk)

            # user video sum
            user_quiz.score += 50
            user_quiz.status = 'FINISH'
            user_quiz.save()
            return Response({'status': 'All OK'})
        else:
            return Response({'user_type': user_type})

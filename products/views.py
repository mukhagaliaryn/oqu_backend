from decimal import Decimal
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles.models import UserQuizData, UserProduct, UserChapter, UserLesson, UserVideo, UserTask, UserAnswer
from products.models import Product, Lesson, Chapter, Video, Task, Question, Answer
from products.serializers import (
    ProductSerializer, ProductChapterSerializer, ProductPurposeSerializer, ProductFeatureSerializer,
    ProductLessonSerializer,
    UserChapterSerializer, UserChapterListSerializer, UserLessonListSerializer, UserLessonSerializer,
    UserVideoSerializer, UserVideoListSerializer, UserTaskSerializer, UserTaskListSerializer,
    UserQuizListSerializer, UserQuizDataSerializer, UserAnswerSerializer,
)


# Product APIView
# ----------------------------------------------------------------------------------------
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

    def post(self, request, pk):
        user_type = request.user.user_type
        user_product = get_object_or_404(UserProduct, product__pk=pk)

        if user_type == 'STUDENT' and not user_product.is_subscribe:
            product = get_object_or_404(Product, pk=pk)
            chapters = product.chapter_set.all()
            lessons = Lesson.objects.filter(chapter__in=chapters)
            videos = Video.objects.filter(lesson__in=lessons)
            tasks = Task.objects.filter(lesson__in=lessons, task_type='WRITE')
            quizzes = Task.objects.filter(lesson__in=lessons, task_type='QUIZ')

            user_product.is_subscribe = True
            user_product.save()
            for chapter in chapters:
                UserChapter.objects.create(user=request.user, chapter=chapter)
            for lesson in lessons:
                UserLesson.objects.create(user=request.user, lesson=lesson)
            for video in videos:
                UserVideo.objects.create(user=request.user, video=video)
            for task in tasks:
                UserTask.objects.create(user=request.user, task=task)
            for quiz in quizzes:
                UserQuizData.objects.create(user=request.user, quiz=quiz, status='START')

            return Response({'status': 'User product and items created!'})
        else:
            return Response({'user_type': user_type})

    def put(self, request, pk):
        user_type = request.user.user_type
        if user_type == 'STUDENT':
            product = get_object_or_404(Product, pk=pk)
            chapters = product.chapter_set.all()
            lessons = Lesson.objects.filter(chapter__in=chapters)
            videos = Video.objects.filter(lesson__in=lessons)
            tasks = Task.objects.filter(lesson__in=lessons, task_type='WRITE')
            quizzes = Task.objects.filter(lesson__in=lessons, task_type='QUIZ')

            for chapter in chapters:
                UserChapter.objects.get_or_create(user=request.user, chapter=chapter)
            for lesson in lessons:
                UserLesson.objects.get_or_create(user=request.user, lesson=lesson)
            for video in videos:
                UserVideo.objects.get_or_create(user=request.user, video=video)
            for task in tasks:
                UserTask.objects.get_or_create(user=request.user, task=task)
            for quiz in quizzes:
                UserQuizData.objects.get_or_create(user=request.user, quiz=quiz)

            return Response({'status': 'User product and items create or updated!'})
        else:
            return Response({'status': 'PUT method worked!'})


# Chapter APIView
# ----------------------------------------------------------------------------------------
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
                'product': product.name,
                'user_chapter': user_chapter_serializer.data,
                'user_chapters': user_chapters_serializer.data,
                'user_lessons': user_lessons_serializer.data,

                'videos': user_videos_serializers.data,
                'tasks': user_tasks_serializers.data,
                'quizzes': user_quizzes_serializers.data,
            }
            return Response(context, status=status.HTTP_200_OK)
        else:
            return Response({'user_type': user_type})


# Lesson APIView
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------

# UserLessonFinish APIView
class UserLessonFinishAPIView(APIView):
    def put(self, request, pk, chapter_pk, lesson_pk):
        user_chapter = get_object_or_404(UserChapter, chapter__pk=chapter_pk)
        user_lesson = get_object_or_404(UserLesson, lesson__pk=lesson_pk)
        user_lessons = UserLesson.objects.filter(lesson__chapter=user_chapter.chapter)

        if not user_lesson.is_done:
            user_lesson.is_done = True
            user_lesson.save()
            user_chapter.score += user_lesson.score / user_lessons.count()
            user_chapter.save()
            return Response({'status': 'User lesson finished!'})
        else:
            return Response({'status': 'User lesson already finished!'})


# Video
# ----------------------------------------------------------------------------------------
class LessonVideoAPIView(APIView):
    def get(self, request, pk, chapter_pk, lesson_pk, video_pk):
        user_type = request.user.user_type
        if user_type == 'STUDENT':
            product = get_object_or_404(Product, pk=pk)
            chapter = get_object_or_404(Chapter, pk=chapter_pk)
            user_lesson = get_object_or_404(UserLesson, lesson__pk=lesson_pk)
            user_video = get_object_or_404(UserVideo, video__pk=video_pk)

            # sidebar
            user_videos = UserVideo.objects.filter(video__lesson=user_lesson.lesson)
            user_tasks = UserTask.objects.filter(task__lesson=user_lesson.lesson)
            user_quizzes = UserQuizData.objects.filter(quiz__lesson=user_lesson.lesson)

            # serializers
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
            user_lesson = get_object_or_404(UserLesson, lesson__pk=lesson_pk)
            user_video = get_object_or_404(UserVideo, video__pk=video_pk)
            user_videos = UserVideo.objects.filter(video__lesson=user_lesson.lesson)

            if not user_video.is_done:
                # user video sum
                user_video.score = 10
                user_video.is_done = True
                user_video.save()

                # sum ball
                if user_lesson.score < 10:
                    user_lesson.score += Decimal(user_video.score)/user_videos.count()
                    user_lesson.save()
                return Response({'status': 'All OK'})
            else:
                return Response({'status': 'Video score already exists'})
        else:
            return Response({'user_type': user_type})


# Task
# ----------------------------------------------------------------------------------------
class LessonTaskAPIView(APIView):

    def get(self, request, pk, chapter_pk, lesson_pk, task_pk):
        user_type = request.user.user_type
        if user_type == 'STUDENT':
            product = get_object_or_404(Product, pk=pk)
            chapter = get_object_or_404(Chapter, pk=chapter_pk)
            user_lesson = get_object_or_404(UserLesson, lesson__pk=lesson_pk)
            user_task = get_object_or_404(UserTask, task__pk=task_pk)

            # sidebar
            user_videos = UserVideo.objects.filter(video__lesson=user_lesson.lesson)
            user_tasks = UserTask.objects.filter(task__lesson=user_lesson.lesson)
            user_quizzes = UserQuizData.objects.filter(quiz__lesson=user_lesson.lesson)

            # serializers
            chapter_serializer = ProductChapterSerializer(chapter, partial=True)
            user_lesson_serializer = UserLessonSerializer(user_lesson, partial=True)
            user_task_serializer = UserTaskSerializer(user_task, partial=True, context={'request': request})

            user_videos_serializers = UserVideoListSerializer(user_videos, many=True)
            user_tasks_serializers = UserTaskListSerializer(user_tasks, many=True)
            user_quizzes_serializers = UserQuizListSerializer(user_quizzes, many=True)

            context = {
                'user_type': user_type,
                'product': product.name,
                'chapter': chapter_serializer.data,
                'user_lesson': user_lesson_serializer.data,
                'user_task': user_task_serializer.data,

                'videos': user_videos_serializers.data,
                'tasks': user_tasks_serializers.data,
                'quizzes': user_quizzes_serializers.data,
            }
            return Response(context, status=status.HTTP_200_OK)
        else:
            return Response({'user_type': user_type})

    def put(self, request, pk, chapter_pk, lesson_pk, task_pk):
        user_type = request.user.user_type
        if user_type == 'STUDENT':
            user_task = get_object_or_404(UserTask, task__pk=task_pk)

            if user_task.status == 'PROGRESS':
                return Response({'status': 'Task status already exists'})
            else:
                user_task.status = 'PROGRESS'
                user_task.save()
                return Response({'status': 'All OK'})
        else:
            return Response({'user_type': user_type})


# Quiz
# ----------------------------------------------------------------------------------------
class LessonQuizAPIView(APIView):
    def get(self, request, pk, chapter_pk, lesson_pk, quiz_pk):
        user_type = request.user.user_type
        if user_type == 'STUDENT':
            product = get_object_or_404(Product, pk=pk)
            chapter = get_object_or_404(Chapter, pk=chapter_pk)
            user_lesson = get_object_or_404(UserLesson, lesson__pk=lesson_pk)
            user_quiz = get_object_or_404(UserQuizData, quiz=quiz_pk)
            user_answers = UserAnswer.objects.filter(user_quiz=user_quiz)

            # sidebar
            user_videos = UserVideo.objects.filter(video__lesson=user_lesson.lesson)
            user_tasks = UserTask.objects.filter(task__lesson=user_lesson.lesson)
            user_quizzes = UserQuizData.objects.filter(quiz__lesson=user_lesson.lesson)

            # serializers
            chapter_serializer = ProductChapterSerializer(chapter, partial=True)
            user_lesson_serializer = UserLessonSerializer(user_lesson, partial=True)
            user_quiz_serializer = UserQuizDataSerializer(user_quiz, partial=True)
            user_answers_serializer = UserAnswerSerializer(user_answers, many=True)

            user_videos_serializers = UserVideoListSerializer(user_videos, many=True)
            user_tasks_serializers = UserTaskListSerializer(user_tasks, many=True)
            user_quizzes_serializers = UserQuizListSerializer(user_quizzes, many=True)

            context = {
                'user_type': user_type,
                'product': product.name,
                'chapter': chapter_serializer.data,
                'user_lesson': user_lesson_serializer.data,
                'user_quiz_data': user_quiz_serializer.data,
                'user_answers': user_answers_serializer.data,

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
            user_lesson = get_object_or_404(UserLesson, lesson__pk=lesson_pk)
            user_quiz = get_object_or_404(UserQuizData, quiz__pk=quiz_pk)

            if user_quiz.status == 'START':
                user_questions = Question.objects.filter(quiz__lesson=user_lesson.lesson).order_by('?')[:5]
                user_quiz.questions.add(*user_questions)
                user_quiz.status = 'PROGRESS'
                user_quiz.save()

                # Create UserAnswer
                for question in user_quiz.questions.all():
                    if question.format == 'MULTI':
                        UserAnswer.objects.create(user_quiz=user_quiz, question=question, max_score=2)
                    else:
                        UserAnswer.objects.create(user_quiz=user_quiz, question=question)

                return Response({'status': 'User quiz method worked'})
            else:
                return Response({'status': 'Quiz already started!'})
        else:
            return Response({'user_type': user_type})


# Choice answer
class LessonQuizChoiceAnswerAPIView(APIView):
    def post(self, request, user_quiz_pk, question_pk, answer_pk):
        user_type = request.user.user_type
        if user_type == 'STUDENT':
            user_quiz = get_object_or_404(UserQuizData, user=request.user, pk=user_quiz_pk)
            question = get_object_or_404(Question, pk=question_pk)
            answer = get_object_or_404(Answer, pk=answer_pk)
            user_answer = get_object_or_404(UserAnswer, user_quiz=user_quiz, question=question)

            if question.format == 'ONE':
                if user_answer.answers.all().count() > 0:
                    user_answer.answers.clear()
                    user_answer.answers.add(answer)
                    return Response({'status': 'Old user answer removed, new added!'})
                else:
                    user_answer.answers.add(answer)
                    return Response({'status': 'Added user answer'})

            elif question.format == 'MULTI':
                if user_answer.answers.filter(id=answer.id).exists():
                    user_answer.answers.remove(answer)
                    return Response({'status': 'Old user answer removed!'})
                else:
                    user_answer.answers.add(answer)
                    return Response({'status': 'User answer added!'})
            else:
                return Response({'status': 'Something error!'})
        else:
            return Response({'user_type': user_type})


# Finish quiz
class LessonQuizFinishAPIView(APIView):
    def put(self, request, pk, chapter_pk, lesson_pk, quiz_pk):
        user_type = request.user.user_type
        if user_type == 'STUDENT':
            user_lesson = get_object_or_404(UserLesson, lesson__pk=lesson_pk)
            user_quiz = get_object_or_404(UserQuizData, quiz__pk=quiz_pk)
            user_quizzes = UserQuizData.objects.filter(quiz__lesson=user_lesson.lesson)

            user_answers = user_quiz.useranswer_set.all()
            correct_count = 0
            for user_answer in user_answers:
                if user_answer.question.format == 'MULTI':
                    if user_answer.answers.filter(answer__correct=False).count() > 1:
                        user_answer.score = 0
                    elif user_answer.answers.filter(answer__correct=False).count() == 1:
                        user_answer.score = 1
                    else:
                        user_answer.score = 2
                else:
                    answer = user_answer.answers.all().first()
                    if answer.correct:
                        user_answer.score = 1

                if user_answer.score:
                    correct_count += 1

            # user video sum
            if not user_quiz.status == 'FINISH':
                x = (correct_count*60) / user_answers.count()
                user_quiz.score = x
                user_quiz.status = 'FINISH'
                user_quiz.save()

                # sum ball
                user_lesson.score += Decimal(user_quiz.score) / user_quizzes.count()
                user_lesson.save()

                return Response({'status': 'All OK'})
            else:
                return Response({'status': 'Quiz score already exists'})
        else:
            return Response({'user_type': user_type})

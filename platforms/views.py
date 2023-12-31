from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from decimal import Decimal

from profiles.models import (
    UserQuizData, UserProduct, UserChapter, UserLesson, UserVideo, UserTask, UserAnswer
)
from products.models import (
    Category, Topic, Lesson, Video, Task, Question, Answer
)
from products.serializers import (
    TopicSerializer, CategorySerializer,
    ProductPurposeSerializer, ProductFeatureSerializer, ProductChapterSerializer, ProductLessonSerializer
)
from platforms.serializers import (
    MainClassGroupSerializer, MainUserProductsSerializer,
    UserChapterUserProductSerializer, UserProductDetailSerializer,
    UserChapterDetailSerializer, UserChapterListSerializer, UserLessonListSerializer, UserLessonSerializer,
    UserVideoSerializer, UserVideoListSerializer, UserTaskSerializer, UserTaskListSerializer,
    UserQuizListSerializer, UserQuizDataSerializer, UserAnswerSerializer, ResultUserAnswerSerializer,
)


# Main API View
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
class MainAPIView(APIView):

    def get(self, request):
        user_type = request.user.user_type

        if user_type == 'STUDENT':
            user = request.user
            class_group = user.classgroup_set.all().first()
            user_products = UserProduct.objects.filter(product__in=class_group.subjects.all(), user=user)
            official = class_group.students.filter(id=user.id).exists()

            class_group_serializer = MainClassGroupSerializer(
                class_group, partial=True, context={'request': request}
            )
            user_products_serializer = MainUserProductsSerializer(
                user_products, many=True, context={'request': request}
            )
            context = {
                'official_student': official,
                'class_group': class_group_serializer.data,
                'user_products': user_products_serializer.data,
            }
            return Response(context, status=status.HTTP_200_OK)
        else:
            return Response({'user_type': user_type})


# Explorer page
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
class ExplorerAPIView(APIView):

    def get(self, request):
        user_type = request.user.user_type

        if user_type == 'STUDENT':
            categories = get_list_or_404(Category, slug='courses')
            topics = get_list_or_404(Topic, category__slug='courses')
            categories_serializers = CategorySerializer(categories, many=True, context={'request': request})
            topics_serializers = TopicSerializer(topics, many=True, context={'request': request})
            context = {
                'user_type': request.user.user_type,
                'categories': categories_serializers.data,
                'topics': topics_serializers.data,
            }
            return Response(context, status=status.HTTP_200_OK)
        else:
            return Response({'user_type': user_type})


# UserProduct page
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
class UserProductAPIView(APIView):

    def get(self, request, user_pk):
        user_type = request.user.user_type
        user_product = get_object_or_404(UserProduct, pk=user_pk)

        if user_type == 'STUDENT':
            purposes = user_product.product.purpose_set.all()
            features = user_product.product.feature_set.all()
            chapters = user_product.product.chapter_set.all()
            lessons = Lesson.objects.filter(chapter__in=chapters)

            user_chapter = UserChapter.objects.filter(
                chapter__product=user_product.product, user=request.user
            ).first() or None
            if user_chapter:
                first_user_chapter_id = user_chapter.id
            else:
                first_user_chapter_id = None

            # serializers
            user_product_serializer = UserProductDetailSerializer(
                user_product, partial=True, context={'request': request}
            )
            purposes_serializer = ProductPurposeSerializer(purposes, many=True)
            features_serializer = ProductFeatureSerializer(features, many=True)
            chapters_serializer = ProductChapterSerializer(chapters, many=True)
            lessons_serializer = ProductLessonSerializer(lessons, many=True)

            context = {
                'user_type': user_type,
                'user_product': user_product_serializer.data,
                'first_user_chapter_id': first_user_chapter_id,
                'purposes': purposes_serializer.data,
                'features': features_serializer.data,
                'chapters': chapters_serializer.data,
                'lessons': lessons_serializer.data
            }
            return Response(context, status=status.HTTP_200_OK)
        else:
            return Response({'user_type': user_type})

    def post(self, request, user_pk):
        user_type = request.user.user_type
        user_product = get_object_or_404(UserProduct, pk=user_pk)

        if user_type == 'STUDENT' and not user_product.is_subscribe:
            product = user_product.product
            chapters = product.chapter_set.all()
            lessons = Lesson.objects.filter(chapter__in=chapters)
            videos = Video.objects.filter(lesson__in=lessons)
            tasks = Task.objects.filter(lesson__in=lessons, task_type='WRITE')
            quizzes = Task.objects.filter(lesson__in=lessons, task_type='QUIZ')

            user_product.is_subscribe = True
            user_product.save()
            for chapter in chapters:
                UserChapter.objects.get_or_create(user=request.user, chapter=chapter)
            for lesson in lessons:
                UserLesson.objects.get_or_create(user=request.user, lesson=lesson)
            for video in videos:
                UserVideo.objects.get_or_create(user=request.user, video=video)
            for task in tasks:
                UserTask.objects.get_or_create(user=request.user, task=task)
            for quiz in quizzes:
                UserQuizData.objects.get_or_create(user=request.user, quiz=quiz, status='START')

            return Response({'status': 'User product and items created!'})
        else:
            return Response({'user_type': user_type})

    def put(self, request, user_pk):
        user_type = request.user.user_type
        user_product = get_object_or_404(UserProduct, pk=user_pk)

        if user_type == 'STUDENT':
            product = user_product.product
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


# UserChapter page
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------
class UserChapterAPIView(APIView):
    def get(self, request, user_pk, user_chapter_pk):
        user_type = request.user.user_type
        user = request.user
        if user_type == 'STUDENT':
            # user chapter data
            user_product = get_object_or_404(UserProduct, pk=user_pk)
            user_chapter = get_object_or_404(UserChapter, pk=user_chapter_pk)
            product = user_product.product
            chapter = user_chapter.chapter

            # sidebar menu
            user_chapters = UserChapter.objects.filter(chapter__product=product, user=user).order_by('chapter')
            user_lessons = UserLesson.objects.filter(lesson__chapter=chapter, user=user).order_by('lesson')

            # chapters list data
            user_videos = UserVideo.objects.filter(video__lesson__chapter=chapter, user=user).order_by('video')
            user_tasks = UserTask.objects.filter(task__lesson__chapter=chapter, user=user).order_by('task')
            user_quizzes = UserQuizData.objects.filter(quiz__lesson__chapter=chapter, user=user).order_by('quiz')

            # serializers
            user_product_serializer = UserChapterUserProductSerializer(user_product, partial=True)
            user_chapter_serializer = UserChapterDetailSerializer(user_chapter, partial=True)
            user_chapters_serializer = UserChapterListSerializer(user_chapters, many=True)
            user_lessons_serializer = UserLessonListSerializer(user_lessons, many=True)

            user_videos_serializers = UserVideoListSerializer(user_videos, many=True)
            user_tasks_serializers = UserTaskListSerializer(user_tasks, many=True)
            user_quizzes_serializers = UserQuizListSerializer(user_quizzes, many=True)

            context = {
                'user_type': user_type,
                'user_product': user_product_serializer.data,
                'user_chapter': user_chapter_serializer.data,
                'user_chapters': user_chapters_serializer.data,
                'user_lessons': user_lessons_serializer.data,

                'user_videos': user_videos_serializers.data,
                'user_tasks': user_tasks_serializers.data,
                'user_quizzes': user_quizzes_serializers.data,
            }
            return Response(context, status=status.HTTP_200_OK)
        else:
            return Response({'user_type': user_type})

    def put(self, request, user_pk, user_chapter_pk):
        user_type = request.user.user_type
        if user_type == 'STUDENT':
            user_product = get_object_or_404(UserProduct, pk=user_pk)
            user_chapter = get_object_or_404(UserChapter, pk=user_chapter_pk)
            user_chapters = UserChapter.objects.filter(chapter__product=user_product.product)

            if not user_chapter.is_done:
                user_chapter.is_done = True
                user_chapter.save()
                user_product.score += Decimal(user_chapter.score) / user_chapters.count()
                user_product.save()
                return Response({'status': 'User chapter finished!'})
            else:
                return Response({'status': 'User chapter already finished!'})
        else:
            return Response({'user_type': user_type})


# UserLesson page
# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------

# UserLessonFinish APIView
class UserLessonFinishAPIView(APIView):
    def put(self, request, user_pk, user_chapter_pk, user_lesson_pk):
        user = request.user
        user_chapter = get_object_or_404(UserChapter, pk=user_chapter_pk)
        user_lesson = get_object_or_404(UserLesson, pk=user_lesson_pk)
        user_lessons = UserLesson.objects.filter(lesson__chapter=user_chapter.chapter, user=user)

        if not user_lesson.is_done:
            user_lesson.is_done = True
            user_lesson.save()
            user_chapter.score += user_lesson.score / user_lessons.count()
            user_chapter.save()
            return Response({'status': 'User lesson finished!'})
        else:
            return Response({'status': 'User lesson already finished!'})


# UserVideo
# ----------------------------------------------------------------------------------------
class UserLessonVideoAPIView(APIView):
    def get(self, request, user_pk, user_chapter_pk, user_lesson_pk, user_video_pk):
        user_type = request.user.user_type
        user = request.user

        if user_type == 'STUDENT':
            user_product = get_object_or_404(UserProduct, pk=user_pk)
            user_chapter = get_object_or_404(UserChapter, pk=user_chapter_pk)
            user_lesson = get_object_or_404(UserLesson, pk=user_lesson_pk)
            user_video = get_object_or_404(UserVideo, pk=user_video_pk)

            # sidebar
            user_videos = UserVideo.objects.filter(video__lesson=user_lesson.lesson, user=user)
            user_tasks = UserTask.objects.filter(task__lesson=user_lesson.lesson, user=user)
            user_quizzes = UserQuizData.objects.filter(quiz__lesson=user_lesson.lesson, user=user)

            # serializers
            chapter_serializer = ProductChapterSerializer(user_chapter.chapter, partial=True)
            user_lesson_serializer = UserLessonSerializer(user_lesson, partial=True)
            user_video_serializer = UserVideoSerializer(user_video, partial=True, context={'request': request})

            user_videos_serializers = UserVideoListSerializer(user_videos, many=True)
            user_tasks_serializers = UserTaskListSerializer(user_tasks, many=True)
            user_quizzes_serializers = UserQuizListSerializer(user_quizzes, many=True)

            context = {
                'user_type': user_type,
                'product': user_product.product.name,
                'chapter': chapter_serializer.data,
                'user_lesson': user_lesson_serializer.data,
                'user_video': user_video_serializer.data,

                'user_videos': user_videos_serializers.data,
                'user_tasks': user_tasks_serializers.data,
                'user_quizzes': user_quizzes_serializers.data,
            }
            return Response(context, status=status.HTTP_200_OK)
        else:
            return Response({'user_type': user_type})

    def put(self, request, user_pk, user_chapter_pk, user_lesson_pk, user_video_pk):
        user_type = request.user.user_type
        user= request.user

        if user_type == 'STUDENT':
            user_lesson = get_object_or_404(UserLesson, pk=user_lesson_pk)
            user_video = get_object_or_404(UserVideo, pk=user_video_pk)
            user_videos = UserVideo.objects.filter(video__lesson=user_lesson.lesson, user=user)

            if not user_video.is_done:
                # user video sum
                user_video.score = 10
                user_video.is_done = True
                user_video.save()

                # sum ball
                user_lesson.score += Decimal(user_video.score) / user_videos.count()
                user_lesson.save()
                return Response({'status': 'Watching video finished!'})
            else:
                return Response({'status': 'Video score already exists'})
        else:
            return Response({'user_type': user_type})


# UserTask
# ----------------------------------------------------------------------------------------
class UserLessonTaskAPIView(APIView):

    def get(self, request, user_pk, user_chapter_pk, user_lesson_pk, user_task_pk):
        user_type = request.user.user_type
        user = request.user

        if user_type == 'STUDENT':
            user_product = get_object_or_404(UserProduct, pk=user_pk)
            user_chapter = get_object_or_404(UserChapter, pk=user_chapter_pk)
            user_lesson = get_object_or_404(UserLesson, pk=user_lesson_pk)
            user_task = get_object_or_404(UserTask, pk=user_task_pk)

            # sidebar
            user_videos = UserVideo.objects.filter(video__lesson=user_lesson.lesson, user=user)
            user_tasks = UserTask.objects.filter(task__lesson=user_lesson.lesson, user=user)
            user_quizzes = UserQuizData.objects.filter(quiz__lesson=user_lesson.lesson, user=user)

            # serializers
            chapter_serializer = ProductChapterSerializer(user_chapter.chapter, partial=True)
            user_lesson_serializer = UserLessonSerializer(user_lesson, partial=True)
            user_task_serializer = UserTaskSerializer(user_task, partial=True, context={'request': request})

            user_videos_serializers = UserVideoListSerializer(user_videos, many=True)
            user_tasks_serializers = UserTaskListSerializer(user_tasks, many=True)
            user_quizzes_serializers = UserQuizListSerializer(user_quizzes, many=True)

            context = {
                'user_type': user_type,
                'product': user_product.product.name,
                'chapter': chapter_serializer.data,
                'user_lesson': user_lesson_serializer.data,
                'user_task': user_task_serializer.data,

                'user_videos': user_videos_serializers.data,
                'user_tasks': user_tasks_serializers.data,
                'user_quizzes': user_quizzes_serializers.data,
            }
            return Response(context, status=status.HTTP_200_OK)
        else:
            return Response({'user_type': user_type})

    def put(self, request, user_pk, user_chapter_pk, user_lesson_pk, user_task_pk):
        user_type = request.user.user_type
        if user_type == 'STUDENT':
            user_task = get_object_or_404(UserTask, pk=user_task_pk)

            if user_task.status == 'PROGRESS':
                return Response({'status': 'Task status already exists'})
            else:
                user_task.status = 'PROGRESS'
                user_task.save()
                return Response({'status': 'All OK'})
        else:
            return Response({'user_type': user_type})


class UserLessonTaskFinishAPIView(APIView):
    def put(self, request, user_pk, user_chapter_pk, user_lesson_pk, user_task_pk):
        user_type = request.user.user_type
        user = request.user

        if user_type == 'STUDENT':
            user_lesson = get_object_or_404(UserLesson, pk=user_lesson_pk)
            user_task = get_object_or_404(UserTask, pk=user_task_pk)
            user_tasks = UserTask.objects.filter(task__lesson=user_lesson.lesson, user=user)

            if user_task.status == 'FINISH':
                return Response({'status': 'Task status already exists'})
            else:
                user_task.status = 'FINISH'
                user_task.save()

                # sum ball
                user_lesson.score += Decimal(user_task.score) / user_tasks.count()
                user_lesson.save()
                return Response({'status': 'Task finished!'})
        else:
            return Response({'user_type': user_type})


# UserQuiz
# ----------------------------------------------------------------------------------------
class UserLessonQuizAPIView(APIView):
    def get(self, request, user_pk, user_chapter_pk, user_lesson_pk, user_quiz_pk):
        user_type = request.user.user_type
        user = request.user

        if user_type == 'STUDENT':
            user_product = get_object_or_404(UserProduct, pk=user_pk)
            user_chapter = get_object_or_404(UserChapter, pk=user_chapter_pk)
            user_lesson = get_object_or_404(UserLesson, pk=user_lesson_pk)
            user_quiz = get_object_or_404(UserQuizData, pk=user_quiz_pk)
            user_answers = UserAnswer.objects.filter(user_quiz=user_quiz)

            # sidebar
            user_videos = UserVideo.objects.filter(video__lesson=user_lesson.lesson, user=user)
            user_tasks = UserTask.objects.filter(task__lesson=user_lesson.lesson, user=user)
            user_quizzes = UserQuizData.objects.filter(quiz__lesson=user_lesson.lesson, user=user)

            # serializers
            chapter_serializer = ProductChapterSerializer(user_chapter.chapter, partial=True)
            user_lesson_serializer = UserLessonSerializer(user_lesson, partial=True)
            user_quiz_serializer = UserQuizDataSerializer(user_quiz, partial=True)

            if user_quiz.status == 'FINISH':
                user_answers_serializer = ResultUserAnswerSerializer(user_answers, many=True)
            else:
                user_answers_serializer = UserAnswerSerializer(user_answers, many=True)

            user_videos_serializers = UserVideoListSerializer(user_videos, many=True)
            user_tasks_serializers = UserTaskListSerializer(user_tasks, many=True)
            user_quizzes_serializers = UserQuizListSerializer(user_quizzes, many=True)

            context = {
                'user_type': user_type,
                'product': user_product.product.name,
                'chapter': chapter_serializer.data,
                'user_lesson': user_lesson_serializer.data,
                'user_quiz_data': user_quiz_serializer.data,
                'user_answers': user_answers_serializer.data,

                'user_videos': user_videos_serializers.data,
                'user_tasks': user_tasks_serializers.data,
                'user_quizzes': user_quizzes_serializers.data,
            }
            return Response(context, status=status.HTTP_200_OK)
        else:
            return Response({'user_type': user_type})

    def put(self, request, user_pk, user_chapter_pk, user_lesson_pk, user_quiz_pk):
        user_type = request.user.user_type
        if user_type == 'STUDENT':
            user_lesson = get_object_or_404(UserLesson, pk=user_lesson_pk)
            user_quiz = get_object_or_404(UserQuizData, pk=user_quiz_pk)

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
class UserLessonQuizChoiceAnswerAPIView(APIView):
    def put(self, request, user_quiz_pk, question_pk, answer_pk):
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
class UserLessonQuizFinishAPIView(APIView):
    def put(self, request, user_pk, user_chapter_pk, user_lesson_pk, user_quiz_pk):
        user_type = request.user.user_type
        user = request.user

        if user_type == 'STUDENT':
            user_lesson = get_object_or_404(UserLesson, pk=user_lesson_pk)
            user_quiz = get_object_or_404(UserQuizData, pk=user_quiz_pk)
            user_quizzes = UserQuizData.objects.filter(quiz__lesson=user_lesson.lesson, user=user)

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
                count = user_answers.count() or 1
                x = (correct_count * user_quiz.max_score) / count
                user_quiz.score = x
                user_quiz.status = 'FINISH'
                user_quiz.save()

                # sum ball
                user_lesson.score += Decimal(user_quiz.score) / user_quizzes.count()
                user_lesson.save()
                return Response({'status': 'Quiz finished!'})
            else:
                return Response({'status': 'Quiz score already exists'})
        else:
            return Response({'user_type': user_type})

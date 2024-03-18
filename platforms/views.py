from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.db.models import Sum

from platforms.serializers.course import CourseSerializer, CoursePurposeSerializer, CourseChapterListSerializer, \
    CourseLessonListSerializer, CourseRatingListSerializer, CourseVideoListSerializer
from platforms.serializers.main import MainHeadlinerCourseListSerializer, MainCourseListSerializer, \
    MainAuthorListSerializer, MainTopicListSerializer
from platforms.serializers.play import PlayVideoSerializer, PlayArticleSerializer, PlayUserCourseSerializer, \
    PlayUserChapterListSerializer, PlayUserLessonListSerializer
from platforms.serializers.topic import TopicSerializer, TopicCourseListSerializer

from accounts.models import Account
from profiles.models import UserCourse, UserChapter, UserLesson
from products.models import Course, Topic, Lesson, Rating, Video, Article


# Main API View
# ----------------------------------------------------------------------------------------------------------------------
class MainAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):
        headliners = Course.objects.filter(is_headline=True)
        last_courses = Course.objects.all()[:8]
        popular_topics = Topic.objects.all()[:5]
        authors = Account.objects.filter(account_type='AUTHOR')[:8]

        headliners_data = MainHeadlinerCourseListSerializer(headliners, many=True, context={'request': request})
        last_courses_data = MainCourseListSerializer(last_courses, many=True, context={'request': request})
        authors_data = MainAuthorListSerializer(authors, many=True, context={'request': request})
        popular_topics_data = MainTopicListSerializer(popular_topics, many=True)

        context = {
            'headliners': headliners_data.data,
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
        last_courses = Course.objects.all()[:48]
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
        authors = Account.objects.filter(account_type='AUTHOR')
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
        topic = get_object_or_404(Topic, slug=slug)
        topic_courses = Course.objects.filter(topic=topic)

        topic_data = TopicSerializer(topic, partial=True, context={'request': request})
        topic_courses_data = TopicCourseListSerializer(topic_courses, many=True, context={'request': request})

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


# CourseDetail API View
# ----------------------------------------------------------------------------------------------------------------------
class CourseDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        purposes = course.purpose_set.all()
        chapters = course.chapter_set.all()
        lessons = Lesson.objects.filter(chapter__in=chapters).order_by('index')
        video = Video.objects.filter(
            lesson__in=Lesson.objects.filter(chapter__in=chapters, access=True))[:3]
        ratings = Rating.objects.filter(course=course).exclude(comment__exact='')

        # Rating counting
        rating_scales = []
        for i in range(1, 6):
            rating_scales.append(Rating.objects.filter(course=course, rating_score=i).count())

        course_data = CourseSerializer(course, partial=True, context={'request': request})
        purposes_data = CoursePurposeSerializer(purposes, many=True)
        chapters_data = CourseChapterListSerializer(chapters, many=True)
        lessons_data = CourseLessonListSerializer(lessons, many=True)
        video_data = CourseVideoListSerializer(video, many=True)
        ratings_data = CourseRatingListSerializer(ratings, many=True, context={'request': request})

        context = {
            'course': course_data.data,
            'course_following_users': UserCourse.objects.filter(course=course).count(),
            'chapters_count': chapters.count(),
            'lessons_count': lessons.count(),
            'all_lesson_duration_sum': lessons.aggregate(Sum('duration'))['duration__sum'],

            'purposes': purposes_data.data,
            'chapters': chapters_data.data,
            'lessons': lessons_data.data,
            'open_video': video_data.data,
            'rating': {
                'users_with_comments': ratings_data.data,
                'rating_scales': rating_scales,
                'all': Rating.objects.filter(course=course).count()
            },
        }

        if request.user.is_authenticated:
            try:
                user_course = UserCourse.objects.get(user=request.user, course=course)
                user_chapter = UserChapter.objects.get(user=request.user, chapter=chapters.first())
                user_lesson = UserLesson.objects.get(user=request.user, lesson=lessons.first())

                context['first_url'] = {
                    'user_course_id': user_course.id,
                    'user_chapter_id': user_chapter.id,
                    'user_lesson_id': user_lesson.id
                }
                context['user_course__course_id'] = user_course.course.id
            except:
                pass
        return Response(context, status=status.HTTP_200_OK)

    def post(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        chapters = course.chapter_set.all()
        lessons = Lesson.objects.filter(chapter__in=chapters)

        UserCourse.objects.get_or_create(course=course, user=request.user)
        for chapter in chapters:
            UserChapter.objects.get_or_create(chapter=chapter, user=request.user)
        for lesson in lessons:
            UserLesson.objects.get_or_create(lesson=lesson, user=request.user)

        return Response({}, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        chapters = course.chapter_set.all()
        lessons = Lesson.objects.filter(chapter__in=chapters)

        for chapter in chapters:
            UserChapter.objects.get_or_create(chapter=chapter, user=request.user)
        for lesson in lessons:
            UserLesson.objects.get_or_create(lesson=lesson, user=request.user)

        return Response({}, status=status.HTTP_201_CREATED)


# CoursePlayerView API View
# ----------------------------------------------------------------------------------------------------------------------
class CoursePlayerView(APIView):

    def get(self, request, course_pk, chapter_pk, lesson_pk):
        user_course = get_object_or_404(UserCourse, pk=course_pk, user=request.user)
        user_chapter = get_object_or_404(UserChapter, pk=chapter_pk, user=request.user)
        user_lesson = get_object_or_404(UserLesson, pk=lesson_pk, user=request.user)

        # For lists
        user_chapters = UserChapter.objects.filter(user=request.user, chapter__in=user_course.course.chapter_set.all())
        user_lessons = UserLesson.objects.filter(
            user=request.user, lesson__chapter__in=user_course.course.chapter_set.all()).order_by('lesson__index')

        context = {}
        if user_lesson.lesson.lesson_type == 'VIDEO':
            video = get_object_or_404(Video, lesson=user_lesson.lesson)
            video_data = PlayVideoSerializer(video, partial=True)
            context['video'] = video_data.data
        elif user_lesson.lesson.lesson_type == 'ARTICLE':
            article = get_object_or_404(Article, lesson=user_lesson.lesson)
            article_data = PlayArticleSerializer(article, partial=True)
            context['article'] = article_data.data

        user_course_data = PlayUserCourseSerializer(user_course, partial=True, context={'request': request})
        # For lists
        user_chapters_data = PlayUserChapterListSerializer(user_chapters, many=True)
        user_lessons_data = PlayUserLessonListSerializer(user_lessons, many=True)

        context['user_course'] = user_course_data.data
        context['user_chapters'] = user_chapters_data.data
        context['user_lessons'] = user_lessons_data.data

        return Response(context, status=status.HTTP_200_OK)

    def put(self, request, course_pk, chapter_pk, lesson_pk):
        user_course = get_object_or_404(UserCourse, pk=course_pk)
        user_chapter = get_object_or_404(UserChapter, pk=chapter_pk)
        user_lesson = get_object_or_404(UserLesson, pk=lesson_pk)
        user_lesson.is_completed = True
        user_lesson.save()
        return Response({'is_completed': user_lesson.is_completed}, status=status.HTTP_204_NO_CONTENT)

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from profiles.models import Profile, UserCourse, UserChapter, UserLesson
from products.models import Course, Topic, Lesson, Rating, Video, Article
from products.serializers import (LastCourseListSerializer, HeadlinerCourseListSerializer,
                                  TopicSerializer, CourseDetailSerializer, PurposeSerializer, LessonListSerializer,
                                  ChapterSerializer, RatingSerializer, VideoSerializer)
from profiles.serializers import (AuthorsListSerializer, UserCourseSerializer, UserLessonSerializer,
                                  UserChapterSerializer
                                  )


# Main API View
# ----------------------------------------------------------------------------------------------------------------------
class MainAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request):
        headliners = Course.objects.filter(is_headline=True)
        last_courses = Course.objects.all()[:8]
        popular_topics = Topic.objects.all()[:5]
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
            context['user'] = request.user.full_name

        return Response(context, status=status.HTTP_200_OK)


# Last courses
# ----------------------------------------------------------------------------------------------------------------------
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
# ----------------------------------------------------------------------------------------------------------------------
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
# ----------------------------------------------------------------------------------------------------------------------
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
        ratings = Rating.objects.filter(course=course).exclude(comment__exact='')

        rating_scales = []
        i = 1
        while i <= 5:
            rating_scales.append(Rating.objects.filter(course=course, rating_score=i).count())
            i += 1

        course_data = CourseDetailSerializer(course, partial=True, context={'request': request})
        purposes_data = PurposeSerializer(purposes, many=True)
        chapters_data = ChapterSerializer(chapters, many=True)
        lessons_data = LessonListSerializer(lessons, many=True)
        ratings_data = RatingSerializer(ratings, many=True, context={'request': request})

        context = {
            'course': course_data.data,
            'purposes': purposes_data.data,
            'chapters': chapters_data.data,
            'lessons': lessons_data.data,
            'rating': {
                'users_with_comments': ratings_data.data,
                'rating_scales': rating_scales,
                'all': Rating.objects.filter(course=course).count()
            },
            'course_following_users': UserCourse.objects.filter(course=course).count()
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
        user_lessons = UserLesson.objects.filter(user=request.user, lesson__chapter__in=user_course.course.chapter_set.all())

        context = {}
        if user_lesson.lesson.lesson_type == 'VIDEO':
            video = get_object_or_404(Video, lesson=user_lesson.lesson)
            video_data = VideoSerializer(video, partial=True)
            context['video'] = video_data.data
        elif user_lesson.lesson.lesson_type == 'ARTICLE':
            article = get_object_or_404(Article, lesson=user_lesson.lesson)
            article_data = VideoSerializer(article, partial=True)
            context['article'] = article_data.data

        user_course_data = UserCourseSerializer(user_course, partial=True, context={'request': request})
        # For lists
        user_chapters_data = UserChapterSerializer(user_chapters, many=True)
        user_lessons_data = UserLessonSerializer(user_lessons, many=True)

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

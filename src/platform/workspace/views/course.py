from django.db.models import Sum
from django.shortcuts import get_object_or_404
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from src.platform.resources.models import Course, Lesson, Video, Rating
from src.platform.workspace.models import UserCourse, UserChapter, UserLesson, Subscribe
from src.platform.workspace.serializers.course import CourseSerializer, PurposeCourseSerializer, \
    ChaptersCourseSerializer, LessonsCourseSerializer, VideoListCourseSerializer, RatingsCourseSerializer


# CourseWorkspace API
# ----------------------------------------------------------------------------------------------------------------------
class CourseWorkspaceAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        purposes = course.purposes.all()
        chapters = course.chapters.all()
        lessons = Lesson.objects.filter(chapter__in=chapters).order_by('order')
        video = Video.objects.filter(
            lesson__in=Lesson.objects.filter(chapter__in=chapters, access=True)
        ).order_by('lesson__order')[:3]
        ratings = Rating.objects.filter(course=course).exclude(comment__exact='')

        # Rating counting
        rating_scales = []
        for i in range(1, 6):
            rating_scales.append(Rating.objects.filter(course=course, assessment=i).count())

        course_data = CourseSerializer(course, partial=True, context={'request': request})
        purposes_data = PurposeCourseSerializer(purposes, many=True)
        chapters_data = ChaptersCourseSerializer(chapters, many=True)
        lessons_data = LessonsCourseSerializer(lessons, many=True)
        video_data = VideoListCourseSerializer(video, many=True)
        ratings_data = RatingsCourseSerializer(ratings, many=True, context={'request': request})

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
            if course.course_type == 'FREE':
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

            elif course.course_type == 'PRO':
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

                try:
                    user_subscribe_course = Subscribe.objects.get(user=request.user, course=course)
                    context['user_subscribe_course_id'] = user_subscribe_course.course.id
                except:
                    pass

            return Response(context, status=status.HTTP_200_OK)
        else:
            return Response(context, status=status.HTTP_200_OK)

    def post(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        chapters = course.chapters.all()
        lessons = Lesson.objects.filter(chapter__in=chapters)

        user_course, created = UserCourse.objects.get_or_create(course=course, user=request.user)
        for chapter in chapters:
            UserChapter.objects.get_or_create(chapter=chapter, user=request.user, user_course=user_course)
        for lesson in lessons:
            UserLesson.objects.get_or_create(lesson=lesson, user=request.user, user_course=user_course)

        return Response({'has_user_course': created}, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        chapters = course.chapters.all()
        lessons = Lesson.objects.filter(chapter__in=chapters)
        user_course, created = UserCourse.objects.get_or_create(course=course, user=request.user)
        for chapter in chapters:
            UserChapter.objects.get_or_create(chapter=chapter, user=request.user, user_course=user_course)
        for lesson in lessons:
            UserLesson.objects.get_or_create(lesson=lesson, user=request.user, user_course=user_course)
        return Response({'has_user_course': created}, status=status.HTTP_201_CREATED)

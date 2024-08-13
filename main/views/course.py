from django.db.models import Sum
from django.shortcuts import get_object_or_404
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from main.models import OldCourse, OldLesson, OldRating, OldUserCourse, OldUserChapter, OldUserLesson, OldSubscribe, OldVideo
from main.serializers.course import CourseSerializer, CoursePurposeSerializer, CourseChapterListSerializer, \
    CourseLessonListSerializer, CourseVideoListSerializer, CourseRatingListSerializer


# CourseDetail API View
# ----------------------------------------------------------------------------------------------------------------------
class CourseDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]

    def get(self, request, pk):
        course = get_object_or_404(OldCourse, pk=pk)
        purposes = course.purpose_set.all()
        chapters = course.chapter_set.all()
        lessons = OldLesson.objects.filter(chapter__in=chapters).order_by('index')
        video = OldVideo.objects.filter(
            lesson__in=OldLesson.objects.filter(chapter__in=chapters, access=True)
        ).order_by('lesson__index')[:3]
        ratings = OldRating.objects.filter(course=course).exclude(comment__exact='')

        # Rating counting
        rating_scales = []
        for i in range(1, 6):
            rating_scales.append(OldRating.objects.filter(course=course, rating_score=i).count())

        course_data = CourseSerializer(course, partial=True, context={'request': request})
        purposes_data = CoursePurposeSerializer(purposes, many=True)
        chapters_data = CourseChapterListSerializer(chapters, many=True)
        lessons_data = CourseLessonListSerializer(lessons, many=True)
        video_data = CourseVideoListSerializer(video, many=True)
        ratings_data = CourseRatingListSerializer(ratings, many=True, context={'request': request})

        context = {
            'course': course_data.data,
            'course_following_users': OldUserCourse.objects.filter(course=course).count(),
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
                'all': OldRating.objects.filter(course=course).count()
            },
        }

        if request.user.is_authenticated:
            if course.course_type == 'FREE':
                try:
                    user_course = OldUserCourse.objects.get(user=request.user, course=course)
                    user_chapter = OldUserChapter.objects.get(user=request.user, chapter=chapters.first())
                    user_lesson = OldUserLesson.objects.get(user=request.user, lesson=lessons.first())

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
                    user_course = OldUserCourse.objects.get(user=request.user, course=course)
                    user_chapter = OldUserChapter.objects.get(user=request.user, chapter=chapters.first())
                    user_lesson = OldUserLesson.objects.get(user=request.user, lesson=lessons.first())

                    context['first_url'] = {
                        'user_course_id': user_course.id,
                        'user_chapter_id': user_chapter.id,
                        'user_lesson_id': user_lesson.id
                    }
                    context['user_course__course_id'] = user_course.course.id
                except:
                    pass

                try:
                    user_subscribe_course = OldSubscribe.objects.get(user=request.user, course=course)
                    context['user_subscribe_course_id'] = user_subscribe_course.course.id
                except:
                    pass

            return Response(context, status=status.HTTP_200_OK)
        else:
            return Response(context, status=status.HTTP_200_OK)

    def post(self, request, pk):
        course = get_object_or_404(OldCourse, pk=pk)
        chapters = course.chapter_set.all()
        lessons = OldLesson.objects.filter(chapter__in=chapters)

        user_course, created = OldUserCourse.objects.get_or_create(course=course, user=request.user)
        for chapter in chapters:
            OldUserChapter.objects.get_or_create(chapter=chapter, user=request.user, user_course=user_course)
        for lesson in lessons:
            OldUserLesson.objects.get_or_create(lesson=lesson, user=request.user, user_course=user_course)

        return Response({'has_user_course': created}, status=status.HTTP_201_CREATED)

    def put(self, request, pk):
        course = get_object_or_404(OldCourse, pk=pk)
        chapters = course.chapter_set.all()
        lessons = OldLesson.objects.filter(chapter__in=chapters)
        user_course, created = OldUserCourse.objects.get_or_create(course=course, user=request.user)
        for chapter in chapters:
            OldUserChapter.objects.get_or_create(chapter=chapter, user=request.user, user_course=user_course)
        for lesson in lessons:
            OldUserLesson.objects.get_or_create(lesson=lesson, user=request.user, user_course=user_course)
        return Response({'has_user_course': created}, status=status.HTTP_201_CREATED)

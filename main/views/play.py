from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import OldUserCourse, OldUserChapter, OldUserLesson, OldVideo, OldArticle
from main.serializers.play import PlayVideoSerializer, PlayArticleSerializer, PlayUserCourseSerializer, \
    PlayUserChapterListSerializer, PlayUserLessonListSerializer


# CoursePlayerView API View
# ----------------------------------------------------------------------------------------------------------------------
class CoursePlayerView(APIView):

    def get(self, request, course_pk, chapter_pk, lesson_pk):
        user_course = get_object_or_404(OldUserCourse, pk=course_pk, user=request.user)
        user_chapter = get_object_or_404(OldUserChapter, pk=chapter_pk, user=request.user)
        user_lesson = get_object_or_404(OldUserLesson, pk=lesson_pk, user=request.user)

        # For lists
        user_chapters = OldUserChapter.objects.filter(user=request.user, chapter__in=user_course.course.chapter_set.all())
        user_lessons = OldUserLesson.objects.filter(
            user=request.user, lesson__chapter__in=user_course.course.chapter_set.all()).order_by('lesson__index')

        context = {}
        if user_lesson.lesson.lesson_type == 'VIDEO':
            video = get_object_or_404(OldVideo, lesson=user_lesson.lesson)
            video_data = PlayVideoSerializer(video, partial=True)
            context['video'] = video_data.data
        elif user_lesson.lesson.lesson_type == 'ARTICLE':
            article = get_object_or_404(OldArticle, lesson=user_lesson.lesson)
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
        user_course = get_object_or_404(OldUserCourse, pk=course_pk)
        user_chapter = get_object_or_404(OldUserChapter, pk=chapter_pk)
        user_lesson = get_object_or_404(OldUserLesson, pk=lesson_pk)
        user_lesson.is_completed = True
        user_lesson.save()
        return Response({'is_completed': user_lesson.is_completed}, status=status.HTTP_204_NO_CONTENT)

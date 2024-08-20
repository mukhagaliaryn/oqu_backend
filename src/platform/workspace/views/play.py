from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from src.platform.resources.models import Video
from src.platform.workspace.models import UserCourse, UserChapter, UserLesson
from src.platform.workspace.serializers.play import PlayVideoSerializer, PlayUserCourseSerializer, \
    PlayUserChapterListSerializer, PlayUserLessonListSerializer


# CoursePlayerWorkspace API
# ----------------------------------------------------------------------------------------------------------------------
class CoursePlayerWorkspaceAPIView(APIView):

    def get(self, request, course_pk, chapter_pk, lesson_pk):
        user_course = get_object_or_404(UserCourse, pk=course_pk, user=request.user)
        user_chapter = get_object_or_404(UserChapter, pk=chapter_pk, user=request.user)
        user_lesson = get_object_or_404(UserLesson, pk=lesson_pk, user=request.user)

        # For lists
        user_chapters = UserChapter.objects.filter(user=request.user, chapter__in=user_course.course.chapters.all())
        user_lessons = UserLesson.objects.filter(
            user=request.user, lesson__chapter__in=user_course.course.chapters.all()
        ).order_by('lesson__order')
        video = get_object_or_404(Video, lesson=user_lesson.lesson)
        video_data = PlayVideoSerializer(video, partial=True)

        user_course_data = PlayUserCourseSerializer(user_course, partial=True, context={'request': request})
        # For lists
        user_chapters_data = PlayUserChapterListSerializer(user_chapters, many=True)
        user_lessons_data = PlayUserLessonListSerializer(user_lessons, many=True)

        context = {
            'user_course': user_course_data.data,
            'user_chapters': user_chapters_data.data,
            'user_lessons': user_lessons_data.data,
            'video': video_data.data
        }
        return Response(context, status=status.HTTP_200_OK)

    def put(self, request, course_pk, chapter_pk, lesson_pk):
        user_course = get_object_or_404(UserCourse, pk=course_pk)
        user_chapter = get_object_or_404(UserChapter, pk=chapter_pk)
        user_lesson = get_object_or_404(UserLesson, pk=lesson_pk)
        user_lesson.is_completed = True
        user_lesson.save()
        return Response({'is_completed': user_lesson.is_completed}, status=status.HTTP_204_NO_CONTENT)

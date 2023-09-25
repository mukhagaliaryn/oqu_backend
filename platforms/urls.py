from django.urls import path
from . import views

urlpatterns = [
    # Main page
    # ----------------------------------------------------------------------------------------
    path('', views.MainAPIView.as_view()),
    path('explorer/', views.ExplorerAPIView.as_view()),

    # Product page
    # ----------------------------------------------------------------------------------------
    path('product/<user_pk>/', views.UserProductAPIView.as_view()),
    # chapter
    path('product/<user_pk>/chapter/<user_chapter_pk>/',
         views.UserChapterAPIView.as_view()),
    # lesson
    path('product/<user_pk>/chapter/<user_chapter_pk>/lesson/<user_lesson_pk>/finished/',
         views.UserLessonFinishAPIView.as_view()),
    # video
    path('product/<user_pk>/chapter/<user_chapter_pk>/lesson/<user_lesson_pk>/video/<user_video_pk>/',
         views.UserLessonVideoAPIView.as_view()),
    # task
    path('product/<user_pk>/chapter/<user_chapter_pk>/lesson/<user_lesson_pk>/task/<user_task_pk>/',
         views.UserLessonTaskAPIView.as_view()),
    path('product/<user_pk>/chapter/<user_chapter_pk>/lesson/<user_lesson_pk>/task/<user_task_pk>/finished/',
         views.UserLessonTaskFinishAPIView.as_view()),
    # quiz
    path('product/<user_pk>/chapter/<user_chapter_pk>/lesson/<user_lesson_pk>/quiz/<user_quiz_pk>/',
         views.UserLessonQuizAPIView.as_view()),
    path('user/quiz/<user_quiz_pk>/question/<question_pk>/answer/<answer_pk>/',
         views.UserLessonQuizChoiceAnswerAPIView.as_view()),
    path('product/<user_pk>/chapter/<user_chapter_pk>/lesson/<user_lesson_pk>/quiz/<user_quiz_pk>/finished/',
         views.UserLessonQuizFinishAPIView.as_view()),
]

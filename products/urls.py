from django.urls import path
from . import views


urlpatterns = [
    path('product/<pk>/', views.ProductAPIView.as_view()),
    # chapter
    path('product/<pk>/chapter/<chapter_pk>/',
         views.ChapterAPIView.as_view()),
    # lesson
    path('product/<pk>/chapter/<chapter_pk>/lesson/<lesson_pk>/finished/',
         views.UserLessonFinishAPIView.as_view()),
    # video
    path('product/<pk>/chapter/<chapter_pk>/lesson/<lesson_pk>/video/<video_pk>/',
         views.LessonVideoAPIView.as_view()),
    # task
    path('product/<pk>/chapter/<chapter_pk>/lesson/<lesson_pk>/task/<task_pk>/',
         views.LessonTaskAPIView.as_view()),
    path('product/<pk>/chapter/<chapter_pk>/lesson/<lesson_pk>/task/<task_pk>/finished/',
         views.LessonTaskFinishAPIView.as_view()),
    # quiz
    path('product/<pk>/chapter/<chapter_pk>/lesson/<lesson_pk>/quiz/<quiz_pk>/',
         views.LessonQuizAPIView.as_view()),
    path('user/quiz/<user_quiz_pk>/question/<question_pk>/answer/<answer_pk>/',
         views.LessonQuizChoiceAnswerAPIView.as_view()),
    path('product/<pk>/chapter/<chapter_pk>/lesson/<lesson_pk>/quiz/<quiz_pk>/finished/',
         views.LessonQuizFinishAPIView.as_view()),
]

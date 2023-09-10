from django.urls import path
from . import views

urlpatterns = [
    path('product/<pk>/', views.ProductAPIView.as_view()),
    path('product/<pk>/chapter/<chapter_pk>/', views.ChapterAPIView.as_view()),

    path('product/<pk>/chapter/<chapter_pk>/lesson/<lesson_pk>/finished/', views.UserLessonFinishAPIView.as_view()),
    path('product/<pk>/chapter/<chapter_pk>/lesson/<lesson_pk>/video/<video_pk>/', views.LessonVideoAPIView.as_view()),
    path('product/<pk>/chapter/<chapter_pk>/lesson/<lesson_pk>/task/<task_pk>/', views.LessonTaskAPIView.as_view()),
    path('product/<pk>/chapter/<chapter_pk>/lesson/<lesson_pk>/quiz/<quiz_pk>/', views.LessonQuizAPIView.as_view()),
]

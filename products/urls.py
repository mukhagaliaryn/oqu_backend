from django.urls import path
from . import views

urlpatterns = [
    path('product/<pk>/', views.ProductAPIView.as_view()),
    path('product/<pk>/chapter/<chapter_pk>/', views.ChapterAPIView.as_view()),
    path('product/<pk>/chapter/<chapter_pk>/lesson/<lesson_id>/video/<video_id>/', views.LessonVideoAPIView.as_view()),
    path('product/<pk>/chapter/<chapter_pk>/lesson/<lesson_id>/task/<task_id>/', views.LessonTaskAPIView.as_view()),
    path('product/<pk>/chapter/<chapter_pk>/lesson/<lesson_id>/quiz/<quiz_id>/', views.LessonQuizAPIView.as_view()),
]

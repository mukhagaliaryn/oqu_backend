from django.urls import path
from . import views

urlpatterns = [
    # main urls
    path('', views.MainAPIView.as_view()),
    path('last-courses/', views.LastCoursesAPIView.as_view()),
    path('authors/', views.AuthorsAPIView.as_view()),
    path('topic/<slug>/', views.TopicAPIView.as_view()),
    path('settings/', views.SettingsAPIView.as_view()),

    # course urls
    path('course/<pk>/', views.CourseDetailAPIView.as_view()),
    path('course/<course_pk>/chapter/<chapter_pk>/lesson/<lesson_pk>/', views.CoursePlayerView.as_view()),
]

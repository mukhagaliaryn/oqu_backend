from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainAPIView.as_view()),
    path('last-courses/', views.LastCoursesAPIView.as_view()),
    path('topic/<slug>/', views.TopicAPIView.as_view()),
]

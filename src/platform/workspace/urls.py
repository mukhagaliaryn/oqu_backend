from django.urls import path
from .views import main
from .views import course
from .views import play


urlpatterns = [
    # main APIs...
    path('', main.MainWorkspaceAPIView.as_view()),
    path('last-courses/', main.LastCoursesWorkspaceAPIView.as_view()),
    path('authors/', main.AuthorsWorkspaceAPIView.as_view()),
    path('subcategory/<slug>/', main.SubcategoryWorkspaceAPIView.as_view()),
    path('settings/', main.SettingsWorkspaceAPIView.as_view()),

    # course APIs...
    path('course/<pk>/', course.CourseWorkspaceAPIView.as_view()),

    # play APIs...
    path('course/<course_pk>/chapter/<chapter_pk>/lesson/<lesson_pk>/', play.CoursePlayerWorkspaceAPIView.as_view()),
]

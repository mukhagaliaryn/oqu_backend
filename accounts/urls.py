from django.urls import path
from . import views


urlpatterns = [
    path('', views.UsersView.as_view()),
    path('user/', views.UserAccountView.as_view()),
    path('user/avatar/', views.UserAvatarAPIView.as_view()),
]

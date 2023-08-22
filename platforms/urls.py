from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainAPIView.as_view()),
    path('explorer/', views.ExplorerAPIView.as_view()),
]

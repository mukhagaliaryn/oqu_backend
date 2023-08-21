from django.urls import path
from .views import index, students

urlpatterns = [
    path('', index.MainAPIView.as_view()),
    path('explorer/', students.ExplorerAPIView.as_view()),
    path('product/<pk>/', students.ProductAPIView.as_view()),
]

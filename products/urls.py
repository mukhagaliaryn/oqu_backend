from django.urls import path
from . import views

urlpatterns = [
    path('product/<pk>/', views.ProductAPIView.as_view()),
]

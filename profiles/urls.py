from django.urls import path
from . import views


urlpatterns = [
    path('user/product/items/create/<product_id>/', views.UserProductItemCreateAPIView.as_view()),

]

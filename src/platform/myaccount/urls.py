from django.urls import path
from .views.main import MainMyAccount

urlpatterns = [
    path('', MainMyAccount.as_view())
]

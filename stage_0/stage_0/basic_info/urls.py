from django.urls import path
from .views import api_info

urlpatterns = [
    path('', api_info),
]
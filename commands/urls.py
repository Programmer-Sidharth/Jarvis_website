from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', home),
    path('jarvis/<str:a>/', response),
    path('friday/<str:a>/', testing),
]

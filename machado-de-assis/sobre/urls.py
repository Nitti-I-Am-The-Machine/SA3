from django.contrib import admin
from django.urls import path
from sobre.views import sobre

urlpatterns = [
    path('sobre/', sobre)
]
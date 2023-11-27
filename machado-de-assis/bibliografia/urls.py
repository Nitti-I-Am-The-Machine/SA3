from django.contrib import admin
from django.urls import path
from bibliografia.views import bibliografia

urlpatterns = [
    path('bibliografia/', bibliografia)
]
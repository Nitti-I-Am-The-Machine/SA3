from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render
from home.views import home
from sobre.views import sobre
from bibliografia.views import bibliografia

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('sobre.urls')),
    path('', include('bibliografia.urls'))
]
"""
URL configuration for djangoProject228 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import random

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from AlexProject_django import settings
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('profile/', views.profile),
    path('about/', views.about),
    path('reg/', views.reg),
    path('auth/', views.auth),
    path('<str:str>/<str:arg2>', views.page404),
]

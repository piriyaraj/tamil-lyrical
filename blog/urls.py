"""Blogging URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('', views.index,name="index"),
    path('test/', views.test, name="test"),
    path('lyrics/<str:path>', views.lyrics, name="lyrics"),
    path('movie/<str:path>', views.movie, name="movie"),
    path('composer/<str:path>', views.composer, name="composer"),
    path('lyricist/<str:path>', views.lyricist, name="lyricist"),
    path('singer/<str:path>', views.singer, name="singer"),
    path('year/<str:path>', views.year, name="year"),
]

componentCallurl=[
    path('get_sidebar/', views.get_sidebar, name="get_sidebar"),
    path('get_newupdate/', views.get_newUpdate, name="get_newupdate"),
]
urlpatterns+=componentCallurl
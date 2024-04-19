
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home , name='home' ),
    path('page/', views.page , name='page' ),
]


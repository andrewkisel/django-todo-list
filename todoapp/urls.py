from django.contrib import admin
from django.urls import path
import django.contrib.auth.views as auth
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:task_id>', views.detail, name='detail'),
]

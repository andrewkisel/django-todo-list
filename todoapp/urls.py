from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:task_id>', views.detail, name='detail'),
    path('new_task/', views.new_task, name='new_task')
]

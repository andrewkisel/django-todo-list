from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Task


# Create your views here.
def index(request):
    tasks = Task.objects.all()
    return render(request, 'todoapp/index.html', context={'tasks': tasks})


def detail(request, task_id):
    task = Task.objects.get(pk=task_id)
    return render(request, 'todoapp/detail.html', context={'task': task})

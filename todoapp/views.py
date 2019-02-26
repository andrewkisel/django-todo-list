from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .models import Task


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        tasks = Task.objects.all()
        return render(request, 'todoapp/index.html', context={'tasks': tasks})
    else:
        return redirect('login')


def detail(request, task_id):
    if request.user.is_authenticated:
        task = get_object_or_404(Task, id=task_id)
        return render(request, 'todoapp/detail.html', context={'task': task})
    else:
        return HttpResponse('Please log in first')

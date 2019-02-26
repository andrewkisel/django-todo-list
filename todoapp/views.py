from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import NewTask


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
        return redirect('login')


def new_task(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = NewTask(request.POST)
            if form.is_valid():
                task = Task.objects.create(
                    task_title=form.cleaned_data.get('task_title'),
                    task_text=form.cleaned_data.get('task_text'),
                    task_priority=form.cleaned_data.get('task_priority'),
                    task_status='AC'
                )
                task.save()
                return redirect('index')
    else:
        return redirect('login')
    return render(request, 'todoapp/new_task.html')
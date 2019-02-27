from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .forms import NewTask, ModifyTask, FilterTask


# Index page.
def index(request):
    if request.user.is_authenticated:
        tasks = Task.objects.all()
        if request.method == 'POST':
            form = FilterTask(request.POST)
            if 'AC' in request.POST:
                tasks = tasks.filter(task_status='AC')
            elif 'IP' in request.POST:
                tasks = tasks.filter(task_status='IP')
            elif 'CD' in request.POST:
                tasks = tasks.filter(task_status='CD')
        return render(request, 'todoapp/index.html', context={'tasks': tasks})
    else:
        return redirect('login')


# Detail page.
def detail(request, task_id):
    if request.user.is_authenticated:
        task = get_object_or_404(Task, id=task_id)
        # Task modification logic.
        if request.method == 'POST':
            form = ModifyTask(request.POST)
            if form.is_valid():
                if 'Save' in request.POST:
                    task.task_title = form.cleaned_data.get('task_title')
                    task.task_text = form.cleaned_data.get('task_text')
                    task.task_priority = form.cleaned_data.get('task_priority')
                    task.task_status = form.cleaned_data.get('task_status')
                    task.save()
                elif 'Delete' in request.POST:
                    task.delete()
                return redirect('index')
        else:
            return render(request, 'todoapp/detail.html', context={'task': task})
    else:
        return redirect('login')


# New task page.
def new_task(request):
    if request.user.is_authenticated:
        # New task creation logic.
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

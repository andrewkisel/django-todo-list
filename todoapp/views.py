from django.shortcuts import render
from django.http import HttpResponse
from .models import Task


# Create your views here.
def index(request):
    tasks = Task.objects.all()
    output = ','.join(q.task_name for q in tasks)
    return HttpResponse(output)


def detail(request, task_id):
    return HttpResponse('This is task #%s' % task_id)

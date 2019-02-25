from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse('This worked!')


def detail(request):
    return HttpResponse('This is details page')

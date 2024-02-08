from django.shortcuts import render
from django.http import HttpResponse

from .decorators import custom_log


@custom_log
def index(request):
    return render(request, 'index.html', {})


@custom_log
def about(request):
    return render(request, 'about.html', {'test': 'test'})


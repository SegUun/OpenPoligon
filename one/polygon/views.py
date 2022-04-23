from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {'title': 'Test'}
    return render(request, 'polygon/index.html', context)

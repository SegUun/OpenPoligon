from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    a = ['--=\/\/-+==-*='*2 for i in range(1000)]
    context = {'title': 'Test', 'test1': ''.join(a)}
    return render(request, 'polygon/index.html', context)

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context = {}
    return render(request, 'catalogueapp/index.html', context)

def adminindex(request):
    context = {}
    return render(request, 'catalogueapp/admin/index.html', context)

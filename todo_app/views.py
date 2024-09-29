from django.shortcuts import render
from django.http import HttpResponse


def todo_app(request):
    return HttpResponse("Hel")
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def todo_app(request):
    result = 10 / 0
    template = loader.get_template("main.html")
    return HttpResponse(template.render())
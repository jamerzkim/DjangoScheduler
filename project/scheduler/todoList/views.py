from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Todo

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def check(request):
    mydata = Todo.objects.all()
    template = loader.get_template('todo.html')
    context = {
        'mymembers': mydata,
    }
    return HttpResponse(template.render(context, request))

def details(request):
    mydata = Todo.objects.all()
    template = loader.get_template('details.html')
    context = {
        'mymembers': mydata,
    }
    return HttpResponse(template.render(context, request))
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Todo
from .forms import InputForm

def main(request):
    
    form = InputForm()
    
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()
            
    context = {
        'form': form
    }
    return render(request, 'main.html', context)

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

def template(request):
    mydata = Todo.objects.all()
    template = loader.get_template('template.html')
    context = {
        'mymembers': mydata,
    }
    return HttpResponse(template.render(context, request))
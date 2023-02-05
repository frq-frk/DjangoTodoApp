from django.shortcuts import render, redirect
from django.http import HttpResponse

from . import models

# Create your views here.

def home(request):
    todoList = models.TodoItem.objects.all()
    return render(request,'index.html',{'list' : todoList})

def addTodo(request):
    obj = models.TodoItem.objects.create(item = request.POST.get('task'))
    return redirect(home)

def delTodo(request, id):
    models.TodoItem.objects.get(id = id).delete()
    return redirect(home)
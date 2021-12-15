from django.shortcuts import render

from .models import Todo

def todo(requst):
    t = Todo.objects.all()
    return render(requst, 'todo.html',{'T' : t})


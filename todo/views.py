from django.shortcuts import render

# Create your views here.

def addTask(request):
    print("Hello")
    return render(request, 'home-todo.html')
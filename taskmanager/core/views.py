from django.shortcuts import render,redirect
from .forms import SignupForm
from task.models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request,'core/index.html',{
        'tasks':tasks,
    })

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()
    return render(request,'core/signup.html',{
       'form':form 
    })   
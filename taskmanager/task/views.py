from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import NewTaskForm,EditTaskForm

@login_required
def detail(request,pk):
    task = get_object_or_404(Task,pk=pk)
    return render(request,'task/detail.html',{
        'task':task,
    })

@login_required
def new(request):
    if request.method == 'POST':
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.created_by = request.user
            task.save()
            return redirect('task:detail',pk=task.id)
    else:
        form = NewTaskForm()
    return render(request,'task/form.html',{
        'form':form,
        'title':'New Task'
    })

@login_required
def delete(request,pk):
    task=get_object_or_404(Task,pk=pk,created_by=request.user)
    task.delete()

    return redirect('core:index.html')

@login_required
def edit(request,pk):
    task=get_object_or_404(Task,pk=pk,created_by=request.user)
    if request.method == 'POST':
        form = EditTaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('task:detail',pk=task.id)
    else:
        form = EditTaskForm(instance=task)
    return render(request,'task/form.html',{
        'form':form,
        'title':'Edit Task'
    })

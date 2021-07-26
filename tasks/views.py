from tasks.forms import TaskForm
from django.shortcuts import redirect, render
from .models import *
from .forms import *

# Create your views here.
def home(request):
    tasks=Tasks.objects.all()
    form=TaskForm
    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")


    context={
        'tasks':tasks,
        'form':form
    }
    return render(request,'tasks/index.html',context)


def update(request,pk):
    task=Tasks.objects.get(id=pk)
    form=TaskForm(instance=task)
    if request.method=='POST':
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect("/")

    context={
        'form': form
    }
    return render(request,'tasks/update.html',context)


def delete(request,pk):
    task=Tasks.objects.get(id=pk)
    if request.method=='POST':
        task.delete()
        return redirect("/")
    
    context={
        'task':task
    }
    return render (request,'tasks/delete.html',context)


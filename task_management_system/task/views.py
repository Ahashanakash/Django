from django.shortcuts import render,redirect
from . import forms
from . import models

# Create your views here.
def add_task(request):
    if request.method=='POST':
        taskform = forms.TaskForm(request.POST)
        if taskform.is_valid():
            taskform.save()   
            return redirect('homepage')
    
    else:
        taskform = forms.TaskForm()
        return render(request,'task.html',{'form': taskform})
    
    
def edit_task(request,id):
    task = models.TaskModel.objects.get(pk = id)
    taskform = forms.TaskForm(instance=task)
    if request.method=='POST':
        taskform = forms.TaskForm(request.POST, instance=task)
        if taskform.is_valid():
            taskform.save()   
            return redirect('homepage')
    
    return render(request,'task.html',{'form': taskform})

def delete_task(request,id):
    task = models.TaskModel.objects.get(pk = id)
    task.delete()
    return redirect('homepage')
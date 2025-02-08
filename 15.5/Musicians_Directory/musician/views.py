from django.shortcuts import render,redirect
from . import forms
from . import models

# Create your views here.
def add_musician(request):
    if request.method=='POST':
        musicianform = forms.musicianform(request.POST)
        if musicianform.is_valid():
            musicianform.save()   
            return redirect('homepage')
    
    else:
        musicianform = forms.musicianform()
        return render(request,'album.html',{'form': musicianform})
    
def edit_musician(request,id):
    musician = models.Musician.objects.get(pk = id)
    musicianform1 = forms.musicianform(instance=musician)
    if request.method=='POST':
        musicianform1 = forms.musicianform(request.POST, instance=musician)
        if musicianform1.is_valid():
            musicianform1.save()   
            return redirect('homepage')
    
    return render(request,'musician.html',{'form': musicianform1})

def delete_musician(request,id):
    musician = models.Musician.objects.get(pk = id)
    musician.delete()
    return redirect('homepage')
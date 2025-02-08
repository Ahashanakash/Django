from django.shortcuts import render,redirect
from . import forms
from . import models

# Create your views here.
def add_album(request):
    if request.method=='POST':
        albumform1 = forms.albumform(request.POST)
        if albumform1.is_valid():
            albumform1.save()   
            return redirect('homepage')
    
    else:
        albumform1 = forms.albumform()
        return render(request,'album.html',{'form': albumform1})
    
def edit_album(request,id):
    album = models.album.objects.get(pk = id)
    albumform1 = forms.albumform(instance=album)
    if request.method=='POST':
        albumform1 = forms.albumform(request.POST, instance=album)
        if albumform1.is_valid():
            albumform1.save()   
            return redirect('homepage')
    
    return render(request,'album.html',{'form': albumform1})

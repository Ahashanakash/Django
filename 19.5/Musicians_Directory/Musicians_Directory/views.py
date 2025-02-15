from django.shortcuts import render
from album.models import album
def home(request):
    data = album.objects.all()
    return render(request,'home.html',{'data':data})
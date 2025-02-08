from django.shortcuts import render,redirect
from . import forms

# Create your views here.
def add_catagory(request):
    if request.method=='POST':
        catagoryform = forms.CatagoryForm(request.POST)
        if catagoryform.is_valid():
            catagoryform.save()   
            return redirect('homepage')
    
    else:
        catagoryform = forms.CatagoryForm()
        return render(request,'catagory.html',{'form': catagoryform})
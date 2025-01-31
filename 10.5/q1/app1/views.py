from django.shortcuts import render

# Create your views here.
def about(request):
    return render(request,'app1/about.html')
def contact(request):
    return render(request,'app1/contact.html')
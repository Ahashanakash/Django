from django.shortcuts import render,redirect
from . import forms
from . import models
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
# def add_album(request):
#     if request.method=='POST':
#         albumform1 = forms.albumform(request.POST)
#         if albumform1.is_valid():
#             albumform1.save()   
#             return redirect('homepage')
#     else:
#         albumform1 = forms.albumform()
#         return render(request,'album.html',{'form': albumform1})
    
@method_decorator(login_required, name='dispatch')
class add_album(CreateView):
    form_class = forms.albumform
    template_name = 'album.html'
    success_url = reverse_lazy('homepage')
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
# def edit_album(request,id):
#     album = models.album.objects.get(pk = id)
#     albumform1 = forms.albumform(instance=album)
#     if request.method=='POST':
#         albumform1 = forms.albumform(request.POST, instance=album)
#         if albumform1.is_valid():
#             albumform1.save()   
#             return redirect('homepage')
    
#     return render(request,'album.html',{'form': albumform1})

@method_decorator(login_required, name='dispatch')
class edit_album(UpdateView):
    model = models.album
    form_class = forms.albumform
    template_name = 'album.html'
    pk_url_kwarg = 'id'
    success_url =reverse_lazy('homepage')
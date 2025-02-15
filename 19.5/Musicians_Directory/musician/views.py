from django.shortcuts import render,redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView, DeleteView
from django.utils.decorators import method_decorator

# Create your views here.
# @login_required
# def add_musician(request):
#     if request.method=='POST':
#         musicianform = forms.musicianform(request.POST)
#         if musicianform.is_valid():
#             # musicianform.cleaned_data['user']= request.user
#             musicianform.instance.user=request.user
#             musicianform.save()   
#             return redirect('add_album')
    
#     else:
#         musicianform = forms.musicianform()
#         return render(request,'album.html',{'form': musicianform})
    
#class based view
@method_decorator(login_required, name='dispatch')
class add_musician(CreateView):
    model = models.Musician
    form_class = forms.musicianform
    template_name = 'album.html'
    success_url = reverse_lazy('add_album')
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
# @login_required
# def edit_musician(request,id):
#     musician = models.Musician.objects.get(pk = id)
#     musicianform1 = forms.musicianform(instance=musician)
#     if request.method=='POST':
#         musicianform1 = forms.musicianform(request.POST, instance=musician)
#         if musicianform1.is_valid():
#             musicianform1.save()   
#             return redirect('homepage')
#     return render(request,'musician.html',{'form': musicianform1})

@method_decorator(login_required, name='dispatch')
class edit_musician(UpdateView):
    model = models.Musician
    form_class = forms.musicianform
    template_name = 'musician.html'
    pk_url_kwarg = 'id'
    success_url =reverse_lazy('homepage')

# @login_required
# def delete_musician(request,id):
#     musician = models.Musician.objects.get(pk = id)
#     musician.delete()
#     return redirect('homepage')

@method_decorator(login_required, name='dispatch')
class delete_musician(DeleteView):
    model = models.Musician 
    template_name = 'delete.html'
    pk_url_kwarg = 'id'
    success_url =reverse_lazy('homepage')
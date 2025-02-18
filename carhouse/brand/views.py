from django.shortcuts import render,redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView, DeleteView
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class add_brand(CreateView):
    model = models.Musician
    form_class = forms.musicianform
    # template_name = 'album.html'
    success_url = reverse_lazy('profile')
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
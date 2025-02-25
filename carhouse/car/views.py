from django.shortcuts import render,redirect,get_object_or_404
from . import forms
from . import models
from django.urls import reverse_lazy,reverse
from django.views.generic import CreateView,UpdateView, DeleteView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Car
from django.contrib import messages

# Create your views here.
@method_decorator(login_required, name='dispatch')
class add_car(CreateView):
    form_class = forms.carform
    success_url = reverse_lazy('homepage')
    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class Car_details(DetailView):
    model = models.Car
    pk_url_kwarg = 'id'
    template_name = 'details.html'
    
    def post(self,request,*args, **kwargs):
        comment_form = forms.commentform(data=self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car = car
            new_comment.save()
        return self.get(request,*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object 
        comments = car.comments.all()  
        comment_form = forms.commentform()

        user_has_purchased = self.request.user.is_authenticated and car.purchased_by == self.request.user
        context['comments'] = comments
        context['comment_form'] = comment_form
        context['user_has_purchased'] = user_has_purchased
        return context

@login_required
def buy_car(request, car_id):
    car = models.Car.objects.get(pk=car_id)

    if car.purchased_by == request.user:
        return redirect('cardetails', id=car_id)
    
    if car.quantity <= 0:
        messages.error(request, "This car is out of stock.")
        return redirect('cardetails', id=car_id)    
    
    else:
        car.purchased_by = request.user
        car.quantity -= 1
        car.save()
        messages.error(request, "Car purchased successfully!")
        
        return redirect ('profile')
    

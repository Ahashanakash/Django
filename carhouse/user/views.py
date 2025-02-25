from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from . import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views.generic import CreateView,UpdateView, DeleteView, ListView
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from car.models import Car

class signup(CreateView):
    model = User
    form_class = forms.RegistrationForm
    template_name = 'user.html'
    success_url = reverse_lazy('log_in')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Account created successfully')
        return response

    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Signup'
        return context
    
class log_in(LoginView):
    template_name = 'user.html'
    # success_url = reverse_lazy('profile')
    
    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request, 'Login successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Incorrect password or useranme')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context

def profile(request):
    data=Car.objects.filter(purchased_by=request.user)
    return render(request,'profile.html',{'data':data})
    
@method_decorator(login_required, name='dispatch')
class edit_profile(UpdateView):
    model = User
    form_class = forms.ChangeUserData
    template_name = 'edit_profile.html'
    pk_url_kwarg = 'id'
    # success_url =reverse_lazy('profile')
    
    def get_object(self, queryset=None):
        return self.request.user
    
    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request, 'profile update successful')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'Error updating profile. Please check the form.')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'update your profile'
        return context

    
@method_decorator(login_required, name='dispatch')
class PasswordChange(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name = 'pass_change.html'
    success_url = reverse_lazy('profile') 

    def form_valid(self, form):
        messages.success(self.request, 'Password updated successfully')
        update_session_auth_hash(self.request, form.user)
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Wrong password or invalid input')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'change password'
        return context
    
@login_required
def log_out(request):
    logout(request)
    messages.success(request, 'Logout Successful')
    return redirect('log_in')

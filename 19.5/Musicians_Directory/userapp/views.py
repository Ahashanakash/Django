from django.shortcuts import render,redirect
from django.contrib import messages
from . import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.views.generic import CreateView,UpdateView, DeleteView
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator

# def signup(request):    
#     if request.method == 'POST':
#         regform = forms.RegistrationForm(request.POST)
#         if regform.is_valid():
#             regform.save()   
#             messages.success(request, 'Account created successfully')
#             return redirect('log_in')
#         else:
#             return render(request, 'user.html', {'form': regform, 'type': 'Signup'})
#     else:
#         regform = forms.RegistrationForm()
#         return render(request, 'user.html', {'form': regform, 'type': 'Signup'})
    
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

# def log_in(request):
#     if request.method=='POST':
#         form = AuthenticationForm(request,request.POST)
#         if form.is_valid():
#             user_name = form.cleaned_data['username']
#             user_pass = form.cleaned_data['password']
#             user = authenticate(username=user_name,password = user_pass)
#             if user is not None:
#                 login(request,user)
#                 messages.success(request,'Login successfully')
#                 return redirect('profile')
#             else:
#                 messages.warning(request,'Incorrect password or useranme')
#                 return redirect('log_in')
#         else:
#             messages.warning(request,'Incorrect password or useranme')
#             return redirect('log_in')
#     else:
#         form = AuthenticationForm()
#         return render(request,'user.html',{'form': form,'type':'Login'})
    
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

# @login_required
# def profile(request):    
#     return render(request, 'profile.html')

@method_decorator(login_required, name='dispatch')
class profile(LoginView):
    template_name = 'profile.html'

# @login_required
# def edit_profile(request):    
#     if request.method=='POST':
#         profileform = forms.ChangeUserData(request.POST,instance = request.user)
#         if profileform.is_valid():
#             profileform.save()   
#             messages.success(request,'profile updated successfully')
#             return redirect('profile')
#         else:
#             messages.error(request, 'Error updating profile. Please check the form.')
#     else:
#         profileform = forms.ChangeUserData(instance=request.user)
#     return render(request, 'edit_profile.html', {'form': profileform})

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

# @login_required
# def PasswordChange(request):    
#     if request.method == 'POST':
#         passform = PasswordChangeForm(request.user, data = request.POST)
#         if passform.is_valid():
#             passform.save()   
#             messages.success(request, 'Password updated successfully')
#             update_session_auth_hash(request, passform.user)
#             return redirect('profile')
#         else:
#             messages.success(request, 'Wrong password')
#             return render(request, 'pass_change.html', {'form': passform, 'type': 'change password'})
#     else:
#         passform = PasswordChangeForm(user=request.user)
#         return render(request, 'pass_change.html', {'form': passform, 'type': 'change password'})
    
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
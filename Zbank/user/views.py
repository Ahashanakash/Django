from django.contrib.auth import authenticate, update_session_auth_hash
from django.shortcuts import render,redirect
from .import forms
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request,'Account created successfully')
            return redirect('log_in')
    else:
        form = forms.SignupForm()
    return render(request, 'signup.html', {'data': form, 'type':'Signup'})


#login
def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']
            user_pass = form.cleaned_data['password']
            user = authenticate(username=user_name,password=user_pass)
            if user is not None:
                messages.success(request,'Logged in successfully')
                login(request,user)
                return redirect('home')
            else:
                messages.error(request,'Log in information incorrect!')
                return redirect('login')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'data': form, 'type':'Log in'})


#profile
@login_required
def profile(request):
    """Display user profile page"""
    account = request.user.account
    
    # Calculate loan statistics
    all_transactions = account.transactions.all()
    pending_loans = all_transactions.filter(
        transaction_type='Loan Request',
        loan_approve=False
    ).count()
    
    approved_loans = all_transactions.filter(
        transaction_type='Loan Request',
        loan_approve=True
    ).count()
    
    return render(request, 'profile.html', {
        'data': None,
        'loan_stats': {
            'pending_loans': pending_loans,
            'approved_loans': approved_loans,
            'total_loans': pending_loans + approved_loans,
        }
    })

@login_required
def log_out(request):
    logout(request)
    messages.success(request, 'Logout Successful')
    return redirect('log_in')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = forms.ChangeUserData(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = forms.ChangeUserData(instance=request.user)
    return render(request, 'edit_profile.html', {'data': form, 'type': 'Edit Profile'})

@login_required
def changepassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,data = request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Password updated successfully')
            update_session_auth_hash(request,form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'password_change.html', {'data': form, 'type':'Update Password'})
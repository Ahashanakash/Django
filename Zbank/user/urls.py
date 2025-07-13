from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.log_in,name='log_in'),
    path('logout/',views.log_out,name='log_out'),
    path('profile/',views.profile,name='profile'),
    path('profile/edit_profile/',views.edit_profile,name='edit_profile'),
    path('edit/pass_channge/',views.changepassword,name='pass_change'),
]
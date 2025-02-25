from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/',views.signup.as_view(),name='signup'),
    path('login/',views.log_in.as_view(),name='log_in'),
    path('logout/',views.log_out,name='log_out'),
    path('profile/',views.profile,name='profile'),
    path('profile/edit_profile/',views.edit_profile.as_view(),name='edit_profile'),
    path('edit/pass_channge/',views.PasswordChange.as_view(),name='pass_change'),
]

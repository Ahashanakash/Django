from django.urls import path
from . import views 

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
    path('password_change/',views.pass_change,name='pass_change'),
    path('password_change2/',views.pass_change2,name='pass_change2'),
]
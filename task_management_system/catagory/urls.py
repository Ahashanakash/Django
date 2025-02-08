from django.urls import path
from . import views

urlpatterns = [
    path('catagory/',views.add_catagory,name='add_catagories'),
]
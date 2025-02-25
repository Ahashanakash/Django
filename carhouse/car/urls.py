from django.urls import path,include
from . import views

urlpatterns = [
    path('cars/',views.add_car.as_view(),name='add_cars'),
    path('cardetails/<int:id>/',views.Car_details.as_view(),name='cardetails'),
    path('buy/<int:car_id>/', views.buy_car, name='buy_car'),
]

from django.urls import path,include
from . import views

urlpatterns = [
    # path('add_musician/',views.add_musician,name='add_musician'),
    path('cars/',views.add_car.as_view(),name='add_cars'),
    path('cardetails/<int:id>/',views.Car_details.as_view(),name='cardetails'),
    path('buy/<int:car_id>/', views.buy_car, name='buy_car'),
    # path('buy/<int:car_id>/', views.buy_car, name='buy_car'),
    # path('edit_musician/<int:id>',views.edit_musician,name='edit_musician'),
    # path('edit_musician/<int:id>/',views.edit_musician.as_view(),name='edit_musician'),
    # path('delete_musician/<int:id>',views.delete_musician,name='delete_musician'),
    # path('delete_musician/<int:id>/',views.delete_musician.as_view(),name='delete_musician'),
]
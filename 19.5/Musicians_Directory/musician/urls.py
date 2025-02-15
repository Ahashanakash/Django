from django.urls import path,include
from . import views

urlpatterns = [
    # path('add_musician/',views.add_musician,name='add_musician'),
    path('add_musician/',views.add_musician.as_view(),name='add_musician'),
    # path('edit_musician/<int:id>',views.edit_musician,name='edit_musician'),
    path('edit_musician/<int:id>/',views.edit_musician.as_view(),name='edit_musician'),
    # path('delete_musician/<int:id>',views.delete_musician,name='delete_musician'),
    path('delete_musician/<int:id>/',views.delete_musician.as_view(),name='delete_musician'),
]
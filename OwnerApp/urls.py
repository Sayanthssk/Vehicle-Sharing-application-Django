

from django.urls import path

from OwnerApp.views import *

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('home', OwnerDash.as_view(), name='home'),
    path('managevehicle', ManageVehicle.as_view(), name='managevehicle'),
    path('addvehicle', AddVehicle.as_view(), name='addvehicle'),
    path('deletevehicle/<int:id>', DeleteVehicle.as_view(), name="deletevehicle"),
    path('editvehicle/<int:id>', EditVehicle.as_view(), name="editvehicle"),
]

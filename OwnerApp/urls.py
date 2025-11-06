

from django.urls import path

from OwnerApp.views import *

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('home', OwnerDash.as_view(), name='home'),
    path('managevehicle', ManageVehicle.as_view(), name='managevehicle'),
]

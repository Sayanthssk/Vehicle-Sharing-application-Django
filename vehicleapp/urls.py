

from django.urls import path

from vehicleapp.views import *

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
]

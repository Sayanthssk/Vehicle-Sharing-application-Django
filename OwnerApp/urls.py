

from django.urls import path

from OwnerApp.views import *

urlpatterns = [
    path('register', RegisterView.as_view(), name='register')
]

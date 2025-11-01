

from django.urls import path

from AdminApp.views import *


urlpatterns = [
    path('adminhome', AdminHome.as_view(), name='adminhome'),
    path('managebus', ManageBusView.as_view(), name='managebus'),
    path('deletebus/<int:id>', DeleteBus.as_view()),
]

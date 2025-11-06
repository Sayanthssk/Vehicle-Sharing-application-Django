

from django.urls import path

from UserApp.views import *

urlpatterns = [
    path('login', LoginPage.as_view()),
    path('reg', UserReg_api.as_view()),
]

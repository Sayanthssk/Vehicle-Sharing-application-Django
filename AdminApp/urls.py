

from django.urls import path

from AdminApp.views import *


urlpatterns = [
    path('adminhome', AdminHome.as_view(), name='adminhome'),
    path('managebus', ManageBusView.as_view(), name='managebus'),
    path('feedback', FeedbackView.as_view(), name='feedback'),
    path('deletebus/<int:id>', DeleteBus.as_view()),
    path('complaints', ComplaintView.as_view(), name='complaints'),
    path('reply/<int:id>', ReplyView.as_view(), name='reply'),
]

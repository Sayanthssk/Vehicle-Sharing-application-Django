from django.shortcuts import render, redirect
from django.views import View

from vehicleapp.forms import *
from vehicleapp.models import *


# Create your views here.

class AdminHome(View):
    def get(self, request):
        c = LoginModel.objects.get(id = request.session['user_id'])
        return render(request, 'adminHome.html', {'c':c})

import random


class ManageBusView(View):
    def get(self, request):
        c = BusModel.objects.all()
        return render(request, 'managebus.html', {'c':c})
    def post(self, request):
        c = BusForm(request.POST, request.FILES)
        if c.is_valid():
            bus = c.save(commit=False)
            
            bus.Latitude = round(random.uniform(8.0, 37.0), 6)
            bus.Longitude = round(random.uniform(68.0, 97.0), 6)

            bus.save()
            return redirect('/AdminApp/managebus')
        

class DeleteBus(View):
    def get(self, request, id):
        c = BusModel.objects.get(id=id)
        c.delete()
        return redirect('/AdminApp/managebus')
    

class FeedbackView(View):
    def get(self, request):
        c = FeedBackModel.objects.all()
        return render(request, 'feedback.html', {'c':c})
    

class ComplaintView(View):
    def get(self, request):
        c = ComplaintModel.objects.all()
        return render(request, 'complaint.html', {'c':c})
    
class ReplyView(View):
    def post(self, request, id):
        c = ComplaintModel.objects.get(id=id)
        reply = ReplyForm(request.POST, instance=c)
        if reply.is_valid():
            reply.save()
            return redirect('/AdminApp/complaints')
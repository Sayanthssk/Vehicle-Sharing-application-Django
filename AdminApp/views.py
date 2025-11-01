from django.shortcuts import render, redirect
from django.views import View

from vehicleapp.forms import *
from vehicleapp.models import *


# Create your views here.

class AdminHome(View):
    def get(self, request):
        c = LoginModel.objects.get(id = request.session['user_id'])
        return render(request, 'adminHome.html', {'c':c})
    

class ManageBusView(View):
    def get(self, request):
        c = BusModel.objects.all()
        return render(request, 'managebus.html', {'c':c})
    def post(self, request):
        c = BusForm(request.POST, request.FILES)
        if c.is_valid():
            c.save()
            return redirect('/AdminApp/managebus')
        

class DeleteBus(View):
    def get(self, request, id):
        c = BusModel.objects.get(id=id)
        c.delete()
        return redirect('//AdminApp/managebus')
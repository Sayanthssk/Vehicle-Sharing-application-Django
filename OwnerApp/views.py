from django.shortcuts import render, redirect
from django.views import View

from vehicleapp.forms import *

# Create your views here.

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')
    def post(self, request):
        c = OwnerForm(request.POST, request.FILES)
        if c.is_valid():
            reg = c.save(commit=False)
            owner = LoginModel.objects.create(Username=reg.Email, Password=request.POST['Password'], UserType="Owner")
            reg.LoginId = owner
            reg.save()
            return redirect('/')
        
class OwnerDash(View):
    def get(self, request):
        c = OwnerModel.objects.get(LoginId__id = request.session['user_id'])
        return render(request, 'home.html', {'c':c})

class ManageVehicle(View):
    def get(self, request):
        c = VehicleModel.objects.all()
        return render(request, 'viewvehicle.html', {'c':c})
    

class AddVehicle(View):
    def get(self, request):
        return render(request, 'addvehicle.html')
    def post(self, request):
        c = VehicleForm(request.POST, request.FILES)
        if c.is_valid():
            reg = c.save(commit=False)
            vehicle=LoginModel.objects.create(Username=request.POST['username'], Password=request.POST['password'], UserType="Vehicle")
            reg.LOGINID = vehicle
            reg.save()
            return redirect('managevehicle')
        
class DeleteVehicle(View):
    def get(self, request, id):
        c = LoginModel.objects.get(id=id)
        c.delete()
        return redirect('managevehicle')
    


class EditVehicle(View):
    def get(self, request, id):
        c = VehicleModel.objects.get(id=id)
        return render(request, 'EditVehicle.html', {'c':c})
    def post(self, request, id):
        c = VehicleModel.objects.get(id=id)
        d = VehicleForm(request.POST, instance=c)
        if d.is_valid():
            d.save()
            return redirect('managevehicle')
        

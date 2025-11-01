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
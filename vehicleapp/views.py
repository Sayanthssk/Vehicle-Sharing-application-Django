from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from vehicleapp.models import *

# Create your views here.

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self, request):
        username = request.POST['Username']
        password = request.POST['Password']
        try:
            login_obj = LoginModel.objects.get(Username=username, Password=password)
            request.session['user_id'] = login_obj.id
            if login_obj.UserType == 'admin':
                return HttpResponse('''<script>alert('Welcome Back !!!');window.location='/AdminApp/adminhome'</script>''')
            elif login_obj.UserType == 'Owner':
                return HttpResponse('''<script>alert('Welcome Back !!!');window.location='/OwnerApp/home'</script>''')
            else:
                return HttpResponse('''<script>alert('invalid User !!!'); window.location='/'</script>''')
        except LoginModel.DoesNotExist:
            return HttpResponse('''<script>alert('Invalid credentials !!!');window.location='/'</script>''')
        

class LogoutView(View):
    def get(self, request):
        return HttpResponse('''<script>alert('Logout SuccessFully');window.location='/'</script>''')
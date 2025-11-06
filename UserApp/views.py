from django.shortcuts import render

# Create your views here.

from django.contrib.auth.hashers import make_password
from UserApp.serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED
)
from vehicleapp.models import *


class LoginPage(APIView):
    def post(self, request):
        response_dict = {}

        # Get data from the request
        username = request.data.get("Username")
        password = request.data.get("Password")

        if not username or not password:
            response_dict["message"] = "failed"
            return Response(response_dict, status=HTTP_400_BAD_REQUEST)

        # Fetch the user
        t_user = LoginModel.objects.filter(Username=username, Password=password).first()

        if not t_user:
            response_dict["message"] = "failed"
            return Response(response_dict, status=HTTP_401_UNAUTHORIZED)

        # Basic success response
        response_dict["message"] = "success"
        response_dict["login_id"] = t_user.id
        response_dict["usertype"] = t_user.UserType

       

        return Response(response_dict, status=HTTP_200_OK)
    


class UserReg_api(APIView):
    def post(self, request):
        print("###################", request.data)

        user_serial = User_Serializer(data=request.data)
        login_serial = LoginSerializer(data=request.data)

        data_valid = user_serial.is_valid()
        login_valid = login_serial.is_valid()

        if data_valid and login_valid:
            login_profile = login_serial.save(UserType='USER')

            # Assign the login profile to the UserTable and save the UserTable
            user_serial.save(LOGINID=login_profile)

            # Return the serialized user data in the response
            return Response(user_serial.data, status=status.HTTP_201_CREATED)

        return Response({
            'login_error': login_serial.errors if not login_valid else None,
            'user_error': user_serial.errors if not data_valid else None
        }, status=status.HTTP_400_BAD_REQUEST)
    
    
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from vehicleapp.models import *

class LoginSerializer(ModelSerializer):
    class Meta:
        model = LoginModel
        fields = '__all__'


class User_Serializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
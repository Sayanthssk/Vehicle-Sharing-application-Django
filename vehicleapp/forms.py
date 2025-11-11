from django.forms import ModelForm

from vehicleapp.models import *

class OwnerForm(ModelForm):
    class Meta:
        model = OwnerModel
        fields = "__all__"


class BusForm(ModelForm):
    class Meta:
        model = BusModel
        fields = '__all__'


class ReplyForm(ModelForm):
    class Meta:
        model = ComplaintModel
        fields = ['reply']

class VehicleForm(ModelForm):
    class Meta:
        model = VehicleModel
        fields = "__all__"
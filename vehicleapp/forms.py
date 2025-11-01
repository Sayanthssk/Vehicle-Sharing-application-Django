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
from django.contrib import admin

from vehicleapp.models import *

# Register your models here.

admin.site.register(LoginModel)
admin.site.register(OwnerModel)
admin.site.register(BusModel)
admin.site.register(UserModel)
admin.site.register(FeedBackModel)
admin.site.register(ComplaintModel)
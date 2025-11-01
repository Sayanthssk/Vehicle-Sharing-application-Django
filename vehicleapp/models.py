from django.db import models

# Create your models here.

class LoginModel(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True)
    Password = models.CharField(max_length=100, null=True, blank=True)
    UserType = models.CharField(max_length=100, null=True, blank=True)


class OwnerModel(models.Model):
    LoginId = models.ForeignKey(LoginModel, on_delete=models.CASCADE, null=True, blank=True)
    Name = models.CharField(max_length=100, null=True, blank=True)
    Phone = models.BigIntegerField(null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    Address = models.TextField(null=True, blank=True)
    ProfilePic = models.ImageField(upload_to='ownerprofile/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name or "Unname user"
    

class BusModel(models.Model):
    Bus_name = models.CharField(max_length=100, null=True, blank=True)
    Bus_no = models.CharField(max_length=100, null=True, blank=True)
    Latitude = models.FloatField(null=True, blank=True)
    Longitude = models.FloatField(null=True, blank=True)
    Source = models.CharField(max_length=100, null=True, blank=True)
    Destination = models.CharField(max_length=100, null=True, blank=True)
    Departure = models.TimeField(null=True, blank=True)
    Arrival = models.TimeField(null=True, blank=True)
    Img = models.ImageField(upload_to='busimage/', null=True, blank=True)
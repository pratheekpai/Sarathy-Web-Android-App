
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class truck_driver(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    fname = models.CharField(max_length=15)
    mname = models.CharField(max_length=15)
    lname = models.CharField(max_length=15)
    date = models.DateField()
    aadhar_no = models.IntegerField(primary_key=True)
    sex = models.CharField(max_length=1)
    address = models.CharField(max_length=50)
    phone = models.IntegerField()

class truck_details(models.Model):
    aadhar_no = models.ForeignKey(truck_driver, on_delete=models.CASCADE)
    license_no = models.CharField(max_length=15, unique=True)
    insurance_no = models.CharField(max_length=15)
    rc_no = models.CharField(max_length=15)  # Registration Certificate Number
    truck_capacity = models.IntegerField()
    permit = models.CharField(max_length=3)
   
class seller_details(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    comp_name = models.CharField(max_length=15)
    comp_address = models.CharField(max_length=50)
    phone = models.IntegerField()
    trade_license_no = models.IntegerField(primary_key=True)


class job_details(models.Model):
    aadhar_no = models.ForeignKey(truck_details, on_delete=models.CASCADE, null=True)
    trade_license_no = models.ForeignKey(seller_details, on_delete=models.CASCADE)
    source = models.CharField(max_length=20, null=True)
    destination = models.CharField(max_length=20, null=True)
    goods_capacity = models.IntegerField(null=True)
    goods = models.CharField(max_length=50, null=True)
    loading_date = models.DateField()
    unloading_date = models.DateField()


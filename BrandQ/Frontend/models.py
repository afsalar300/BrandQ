from django.db import models

# Create your models here.
class loginsavedb(models.Model):
    user_name = models.CharField(max_length=100, null=True, blank=True)
    user_email = models.CharField(max_length=100, null=True, blank=True)
    user_password = models.CharField(max_length=100, null=True, blank=True)

class orderdb(models.Model):
    Country = models.CharField(max_length=100, null=True, blank=True)
    First_Name = models.CharField(max_length=100, null=True, blank=True)
    Last_Name = models.CharField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    Apartment = models.CharField(max_length=100, null=True, blank=True)
    State = models.CharField(max_length=100, null=True, blank=True)
    Postal_Zip = models.CharField(max_length=100, null=True, blank=True)
    Email_Address = models.CharField(max_length=100, null=True, blank=True)
    Phone = models.IntegerField(null=True, blank=True)
    Product = models.CharField(max_length=100, null=True, blank=True)
    Quantity = models.CharField(max_length=100, null=True, blank=True)
    Price = models.CharField(max_length=100, null=True, blank=True)

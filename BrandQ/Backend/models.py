from django.db import models
from django import forms

# Create your models here.
class categorydb(models.Model):
    ca_name = models.CharField(max_length=100, null=True, blank=True)
    ca_description = models.CharField(max_length=100, null=True, blank=True)
    ca_image = models.ImageField(upload_to='category', null=True, blank=True)

class category2(models.Model):
    ca2_name = models.CharField(max_length=100, null=True, blank=True)
    ca2_description = models.CharField(max_length=100, null=True, blank=True)
    ca2_image = models.ImageField(upload_to='category2', null=True, blank=True)

class productdb(models.Model):
    cat_name = models.CharField(max_length=100, null=True, blank=True)
    pro_name = models.CharField(max_length=100, null=True, blank=True)
    pro_description = models.CharField(max_length=100, null=True, blank=True)
    pro_price = models.CharField(max_length=100,null=True, blank=True)
    pro_stock = models.IntegerField(null=True, blank=True)
    pro_product_image = models.ImageField(upload_to='product', null=True, blank=True)
    pro_product_imagee = models.ImageField(upload_to='product', null=True, blank=True)
    pro_product_imageee = models.ImageField(upload_to='product', null=True, blank=True)


class cart_data(models.Model):
    Useremail = models.CharField(max_length=100, null=True, blank=True)
    p_name = models.CharField(max_length=100, null=True, blank=True)
    p_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    p_size = models.CharField(max_length=100, null=True, blank=True)
    p_quantity = models.IntegerField(null=True, blank=True)
    price_total = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    p_image = models.ImageField(upload_to='cart_detail', null=True, blank=True)

class contactDB(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=400)
    message = models.CharField(max_length=400)
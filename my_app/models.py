from django.db import models
from django.db.models import Model
from django.shortcuts import render
# from .forms import FormContactForm


# Create your models here.
class CustomUser(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    password = models.CharField(max_length = 50 , null = True)
    # passwordrepeat = models.CharField(max_length = 50, null = True)
    class Meta:
        db_table = "users"

class Gallery(models.Model):
    upload = models.ImageField(upload_to ='uploads/')
    description = models.CharField(max_length=150)
    class Meta:
        db_table = "Gallery"
        

class Students(models.Model):
    roll_no = models.IntegerField()
    name = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=12)
    description = models.CharField(max_length=50)
    stream = models.CharField(max_length=30)
    class Meta:
        db_table = "Student"


class Staff(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    email =  models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=12)
    exp  = models. DateTimeField(null=True, blank=True)
    photo = models.ImageField(upload_to ='uploads/')
    class Meta:
        db_table="Staff"


class Contact_us(models.Model):
    name = models.CharField(max_length=30)
    email =  models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=12)
    message = models.CharField(max_length=200)
    class Meta:
        db_table="Contact_us"


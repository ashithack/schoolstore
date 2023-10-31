from django.db import models
class Formdatas(models.Model):
    name = models.CharField(max_length=250, default='some_value')
    dob = models.DateField(default='some_value')
    age = models.IntegerField(default='some_value')
    gender = models.CharField(max_length=12, default='some_value')
    phone = models.CharField(max_length=10,default='some_value')
    email = models.CharField(max_length=250, default='some_value')
    address = models.CharField(max_length=250,default='some_value')
    dept = models.CharField(max_length=50,default='some_value')
    course = models.CharField(max_length=50, default='some_value')
# Create your models here.

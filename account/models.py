from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
    
    user_id = models.ForeignKey(User , on_delete = models.CASCADE)
    fname = models.CharField(max_length = 50 , default = "")
    lname = models.CharField(max_length = 50 , default = "")
    address = models.CharField(max_length = 100 , default = "")
    mobile_number = models.CharField(max_length = 10 , default = "")
    zipcode = models.CharField(max_length = 10 , default = "")
    town = models.CharField(max_length = 15 , default = "")
    state = models.CharField(max_length = 20 , default = "")
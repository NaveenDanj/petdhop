from django.db import models
from uuid import uuid4
from django.contrib.auth.models import User
from product.models import Product

def gen_uuid() -> str:
    """Return a str representation of a uuid4"""
    return str(uuid4())
# Create your models here.

class Order(models.Model):
    order_id = models.CharField(unique=True,
            primary_key=True,
            default=gen_uuid,
            max_length=36)
    user_id = models.ForeignKey(User , on_delete = models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True , null = True)
    total = models.IntegerField(default = 0)
    status = models.CharField(max_length = 10 , default = 'Pending')

class Order_Product(models.Model):
    order_id = models.ForeignKey(Order , on_delete = models.CASCADE)
    product_id = models.ForeignKey(Product , on_delete = models.CASCADE)
    amount = models.IntegerField(default = 0)
    total = models.IntegerField(default = 0)
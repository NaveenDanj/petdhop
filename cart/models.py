from django.db import models
from django.contrib.auth.models import User
from product.models import Product
# Create your models here.


class Cart(models.Model):
    user_id = models.ForeignKey(User , on_delete = models.CASCADE)
    product_id = models.ForeignKey(Product , on_delete = models.CASCADE)
    amount = models.IntegerField(default = 1)
    total = models.IntegerField(default = 0)
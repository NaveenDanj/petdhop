from django.db import models
from django.contrib.auth.models import User
from product.models import Product
# Create your models here.
from uuid import uuid4


def gen_uuid() -> str:
    return str(uuid4())


class Wishlist(models.Model):
    wish_id = models.CharField(unique=True,
            primary_key=True,
            default=gen_uuid,
            max_length=36)
    user_id = models.ForeignKey(User , on_delete = models.CASCADE)
    product_id = models.ForeignKey(Product , on_delete = models.CASCADE)
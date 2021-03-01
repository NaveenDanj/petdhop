from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4



def gen_uuid() -> str:
    """Return a str representation of a uuid4"""
    return str(uuid4())



class Product(models.Model):
    pid = models.CharField(unique=True,
            primary_key=True,
            default=gen_uuid,
            max_length=36)

    name = models.CharField(max_length = 200)
    old_price = models.IntegerField()
    new_price = models.IntegerField()
    short_desc = models.TextField()
    long_desc = models.TextField()
    tags = models.TextField()
    stocks = models.IntegerField(default = 0)
    total_sales = models.IntegerField(default = 0)



class Comment(models.Model):
    cid = models.CharField(unique=True,
            primary_key=True,
            default=gen_uuid,
            max_length=36)
    pid = models.ForeignKey(Product , on_delete=models.CASCADE)
    userid = models.ForeignKey(User , on_delete=models.CASCADE)
    comment = models.CharField(max_length = 500 , blank = False , null = False)
    ratings = models.IntegerField(default = 0)
    added_date = models.CharField(max_length = 50 , default = '1')


class Image(models.Model):

    image_id = models.CharField(unique=True,
            primary_key=True,
            default=gen_uuid,
            max_length=36)

    image_file = models.ImageField(null = True , blank = True , upload_to = 'uploads/')
    date_added = models.DateTimeField(auto_now_add=True , null = True)


class Product_Image(models.Model):
    product_id = models.ForeignKey(Product , on_delete = models.CASCADE)
    image_id = models.ForeignKey(Image , on_delete = models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True , null = True)


class Category(models.Model):
    category_id = models.CharField(unique=True,
            primary_key=True,
            default=gen_uuid,
            max_length=36)

    cat_name = models.CharField(max_length = 100)
    cat_img = models.ImageField(null = True , blank = True , upload_to = 'category_img/')

class Product_Category(models.Model):

    product_id = models.ForeignKey(Product , on_delete = models.CASCADE)
    cat_id = models.ForeignKey(Category , on_delete = models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True , null = True)



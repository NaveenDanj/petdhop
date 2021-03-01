from django.db import models
from uuid import uuid4



def gen_uuid() -> str:
    """Return a str representation of a uuid4"""
    return str(uuid4())


class Notification(models.Model):

    notify_id = models.CharField(unique=True,
            primary_key=True,
            default=gen_uuid,
            max_length=36)

    notify_type = models.CharField(max_length = 20)
    date_added = models.DateTimeField(auto_now_add=True , null = True)
    notify_text = models.CharField(max_length = 75 , null = False)
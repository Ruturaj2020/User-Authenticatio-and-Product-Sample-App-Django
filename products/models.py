from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class productview(models.Model):
    product_name = models.CharField(max_length=50)
    weight = models.IntegerField()
    price = models.IntegerField()
    updated_time = models.DateTimeField(auto_now=True)
    created_time = models.DateTimeField(auto_now_add=True)
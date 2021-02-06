from django.db import models
from django.contrib.auth.models import User
from inventory.models import Destination

# Create your models here.

class Items(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    item_name = models.CharField(max_length=50)
    price = models.IntegerField() 
    quantity = models.IntegerField()
    category = models.CharField(max_length=50)
from django.db import models
from django.forms import CharField, IntegerField

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=100, default='')
    quantity = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.name
        

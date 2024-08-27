from django.db import models
from products.models import *

# Create your models here.

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    products = models.ManyToManyField(ManufacturedProduct)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=20)

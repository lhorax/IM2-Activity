from django.db import models
from customer.models import *
from product.models import *
# Create your models here.

class Purchase(models.Model):
    datePurchased = models.DateField(auto_now_add=True)
    quantity = models.IntegerField()
    totalPrice = models.FloatField()
    customerID = models.ForeignKey(Customer, null = False, blank = False, on_delete = models.CASCADE)
    productID = models.ForeignKey(Product, null = False, blank = False, on_delete = models.CASCADE)

    class Meta:
    	db_table = "Purchase"
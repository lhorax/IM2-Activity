from django.db import models

# Create your models here.
class Purchase(models.Model):
    date = models.DateField(auto_now_add=True)
    customerID = models.IntegerField()
    productID = models.IntegerField()

from django.db import models
from datetime import datetime

# Create your models here.

class Product(models.Model):
	dateRegistered = models.DateField(auto_now=True, null = False, blank = False)
	sku = models.CharField(max_length = 6, null = False, blank = False)
	category = models.CharField(max_length = 50)
	name = models.CharField(max_length = 50, null = False, blank = False)
	brand = models.CharField(max_length = 50)
	color = models.CharField(max_length = 50)
	size = models.CharField(max_length = 10)
	unitPrice = models.FloatField()
	quantity = models.IntegerField()

	class Meta:
		db_table = "Product"

class ProductImages(models.Model):
	product = models.ForeignKey(Product, null = False, blank = False, on_delete = models.CASCADE)
	productImage = models.ImageField()

	class Meta:
		db_table = "Product_Images"




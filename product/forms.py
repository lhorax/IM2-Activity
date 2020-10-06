from django import forms
from .models import *

class ProductForm(forms.ModelForm):

	class Meta:
		model = Product
		fields = ('name','unitPrice','quantity')

class ProductImagesForm(forms.ModelForm):

	class Meta:
		model = ProductImages
		fields = ('productImage',)
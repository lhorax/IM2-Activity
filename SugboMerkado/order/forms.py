from django import forms
from .models import *

class PurchaseForm(forms.ModelForm):
	class Meta:
		model = Purchase
		fields = ('customerID',)
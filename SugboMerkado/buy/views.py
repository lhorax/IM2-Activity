from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.contrib import messages
from .models import *
from customer.models import *
from product.models import *

# Create your views here.
class BuyIndexView(View):
    def get(self,request):
        cid = request.session.get('cid')
        customer = Person.objects.get(id = cid)
        qsproducts = Product.objects.all()
        for prod in qsproducts:
            prod.ProductImages = ProductImages.objects.filter(product_id = prod.id)

        context = {
            'customer':customer,
            'products':qsproducts,
        }
        return render(request, 'buy/buy.html',context)

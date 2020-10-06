from django.shortcuts import render,redirect
from django.views.generic import View, TemplateView
from django.contrib import messages
from .models import *
from customer.models import *
from product.models import *
from .forms import *

# Create your views here.
list = []
class OrderIndexView(View):
    def get(self,request):
        cid = request.session.get('cid')
        if len(list) == 0:
            list.append('c'+cid)
        elif list[0] != 'c'+cid:
            list.clear()
            list.append('c'+cid)
        customer = Person.objects.get(id = cid)
        qsproducts = Product.objects.all()
        for prod in qsproducts:
            prod.ProductImages = ProductImages.objects.filter(product_id = prod.id)

        context = {
            'customer':customer,
            'products':qsproducts,
        }
        return render(request, 'orders/order.html',context)

    def post(self, request):
        if request.method == 'POST':
            if 'addToCart' in request.POST:
                prodId = request.POST.get('prodID')
                if not prodId in list:
                    list.append(prodId)
                return redirect('order:index_view')
            if 'cancelPurchaseBtn' in request.POST:
                list.clear()
                return redirect('customer:index_view')
            if 'cartBtn' in request.POST:
                return redirect('order:cart_view')


class OrderListView(View):
    def get(self, request):
        cid = request.session.get('cid')
        qsproducts = []
        count = 1;
        for x in list:
            if count != 1:
                qsproducts.append(Product.objects.get(id = x))
            count=count+1
        
        context = {
            'productItems' : qsproducts,
        }
        return render(request, 'orders/orderList.html',context)

    def post(self, request):
        if 'addMoreBtn' in request.POST:
            return redirect('order:index_view')

        if 'btnProceed' in request.POST:
            cid = request.session.get('cid')
            form = PurchaseForm(request.POST)
            datePurchased = request.POST.get('datePurchased')
            customerObj = Customer.objects.get(id = cid)
            prodIds = request.POST.getlist('prodID')
            quantity = request.POST.getlist('qty')
            i=0
            for prodId in prodIds:
                productObj = Product.objects.get(id = prodId)
                if i < len(quantity):
                    productObj.quantity = productObj.quantity - int(quantity[i])
                    productObj.save()
                    for qty in range(int(quantity[i])):
                        form = Purchase(datePurchased = datePurchased, customerID = customerObj, productID = productObj)
                        form.save()

                i = i+1
            list.clear()
            return redirect('order:cart_view')

        if 'removeItem' in request.POST:
            item = request.POST.get('removeItem')
            list.remove(item)
            return redirect('order:cart_view')

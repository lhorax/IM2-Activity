from django.shortcuts import render,redirect
from django.views.generic import View, TemplateView
from django.contrib import messages
from django.db.models import Count
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
        category = request.session.get('category')

        if category == 'Men':
            qsproducts = Product.objects.filter(quantity__gt=0).filter(category=category)
        elif category =='Women':
            qsproducts = Product.objects.filter(quantity__gt=0).filter(category=category)
        else:
            qsproducts = Product.objects.filter(quantity__gt = 0)

        for prod in qsproducts:
            prod.ProductImages = ProductImages.objects.filter(product_id = prod.id)

        context = {
            'customer':customer,
            'products':qsproducts,
        }
        return render(request, 'orders/index.html',context)

    def post(self, request):
        if request.method == 'POST':
            if 'addToCart' in request.POST:
                prodId = request.POST.get('prodID')
                if not prodId in list:
                    list.append(prodId)
                messages.success(request, 'added successful!', extra_tags='toast')
                return redirect('order:index_view')
            if 'cancelPurchaseBtn' in request.POST:
                list.clear()
                return redirect('customer:index_view')
            if 'cartBtn' in request.POST:
                return redirect('order:cart_view')
            if 'Unisex' in request.POST:
                category = request.POST.get("categoryUnisex")
                request.session['category'] = category
                return redirect('order:index_view')
            if 'Men' in request.POST:
                category = request.POST.get("categoryMen")
                request.session['category'] = category
                return redirect('order:index_view')
            if 'Women' in request.POST:
                category = request.POST.get("categoryWomen")
                request.session['category'] = category
                return redirect('order:index_view')


class OrderListView(View):
    def get(self, request):
        cid = request.session.get('cid')
        customer = Person.objects.get(id = cid)
        qsproducts = []
        count = 1
        for x in list:
            if count != 1:
                qsproducts.append(Product.objects.get(id = x))
            count=count+1
        
        context = {
            'productItems' : qsproducts,
            'customer' : customer,
        }
        return render(request, 'orders/order.html',context)

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
            totalPrice = request.POST.getlist('totalPrice')
            i=0
            for prodId in prodIds:
                productObj = Product.objects.get(id = prodId)
                productObj.quantity = productObj.quantity - int(quantity[i])
                productObj.save()
                form = Purchase(datePurchased = datePurchased, quantity = quantity[i], totalPrice = float(totalPrice[i]), customerID = customerObj, productID = productObj)
                form.save()
                i = i+1
            list.clear()
            messages.success(request, 'Purchase successful!', extra_tags='save')
            return redirect('order:index_view')

        if 'removeItem' in request.POST:
            item = request.POST.get('removeItem')
            list.remove(item)
            return redirect('order:cart_view')

class OrderedProductsView(View):
    def get(self, request):
        cid = request.session.get('cid')
        qscustomer = Person.objects.get(id = cid)
        qspurchase = Purchase.objects.filter(customerID = cid)
        for prod in qspurchase:
            prod.ProductImages = ProductImages.objects.filter(product_id = prod.productID.id)

        context = {
            'customer' : qscustomer,
            'purchase' : qspurchase,
        }
        return render(request, 'orders/orderList.html',context)

class ProductsCategoryView(View):
    def get(self, request):
        return HttpResponse('hi')
    def post(self, request):
        if 'Unisex' in request.Post:
            return render(request, 'orders/orderList.html')
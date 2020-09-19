from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.contrib import messages
from .functions import getSku
from .models import *
from .forms import *

# Create your views here.

class ProductIndexView(View):
	def get(self, request):
		return render(request, 'product/product.html')

	def post(self,request):
		if(request.method == 'POST'):
			if 'addProdBtn' in request.POST:
				return redirect('product:registration_view')
			if 'btnUpdateProduct' in request.POST:
				return render(request, 'product/product.html')
			if 'btnDelete' in request.POST:
				return render(request, 'product/product.html')

class ProductRegistrationView(View):
	
	def get(self, request):
		data = Product()
		pid = Product.objects.last()
		num = 0
		if str(pid) == "None":
			num = 1
		else:
			temp = str(pid)[16:-1]
			num = int(temp)+1
		sku = getSku(num)
		messages.success(request,""+sku, extra_tags='skuID')
		return render(request, 'product/productRegistration.html')

	def post(self, request):
		form = ProductForm(request.POST)
		form2 = ProductImagesForm(request.POST, request.FILES)

		if (form.is_valid() and form2.is_valid()):
			date = request.POST.get('dateRegistered')
			sku = request.POST.get('sku')
			category = request.POST['category']
			name = request.POST.get('name')
			brand = request.POST.get('brand')
			color = request.POST.get('color')
			size = request.POST.get('size')
			unitPrice = request.POST.get('unitPrice')
			quantity = request.POST.get('quantity')
			form = Product(dateRegistered = date, sku = sku, category = category, name = name, brand = brand, color = color, size = size, unitPrice = unitPrice, quantity = quantity)
			form.save()

			productImage = request.FILES['productImage']
			form2 = ProductImages(product = form, productImage=productImage)
			form2.save()
			if request.FILES.get('productImage2',False) != False:
				productImage = request.FILES['productImage2']
				form2 = ProductImages(product = form, productImage=productImage)
				form2.save()
			if request.FILES.get('productImage3', False) != False:
				productImage = request.FILES['productImage3']
				form2 = ProductImages(product = form, productImage=productImage)
				form2.save()
			messages.success(request, 'Product record saved!', extra_tags='save')
			return redirect('product:registration_view')
		else:
			messages.error(request, 'Not Valid!', extra_tags='error')
			return redirect('product:registration_view')
					


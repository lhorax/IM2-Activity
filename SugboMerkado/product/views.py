from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.contrib import messages
from .functions import getSku
from .models import *
from .forms import *
from django.db.models import Count
from django.db.models.functions import TruncMonth

# Create your views here.

class ProductIndexView(View):
	def get(self, request):
		qsproducts = Product.objects.filter(isdeleted = False);
		
		for prod in qsproducts:
			prod.ProductImages = ProductImages.objects.filter(product_id = prod.id)

		# Product chart
		chartProduct = (Product.objects.filter(isdeleted = False).
			extra(
				select = {
					'month':"EXTRACT(month FROM dateRegistered)",
					'year': "EXTRACT(year FROM dateRegistered)",
				}
			).values('month','year').annotate(count_items = Count('dateRegistered'))
		)

		# 0 registrants as default for for 12 months 
		valProduct = [0,0,0,0,0,0,0,0,0,0,0,0]
		
		for c in chartProduct:
			valProduct[c['month']-1] += c['count_items']

		context = {
			'products':qsproducts,
			'valProduct': valProduct,
		}

		return render(request, 'product/product.html',context)

	def post(self,request):
		if(request.method == 'POST'):
			if 'addProdBtn' in request.POST:
				return redirect('product:registration_view')

			if 'btnUpdateProduct' in request.POST:
				prodId = request.POST.get('prodID')
				category = request.POST['pCategory']
				name = request.POST.get('pName')
				brand = request.POST.get('pBrand')
				color = request.POST.get('pColor')
				size = request.POST.get('pSize')
				unitPrice = request.POST.get('unitPrice')
				quantity = request.POST.get('qty')
				update_product = Product.objects.filter(id = prodId).update(category = category, name = name, brand = brand, color = color, size = size, unitPrice = unitPrice, quantity = quantity)
				
				imgIds = request.POST.getlist('imgID')
				count = 0
				for x in imgIds:
					count = count+1

				if request.FILES.get('productImage1',False) != False:
					update_img = ProductImages.objects.get(id = imgIds[0])
					update_img.productImage.delete()
					update_img.productImage = request.FILES['productImage1']
					update_img.save()

				if request.FILES.get('productImage2',False) != False:
					if(count == 2):
						update_img = ProductImages.objects.get(id = imgIds[1])
						update_img.productImage.delete()
						update_img.productImage = request.FILES['productImage2']
						update_img.save()
					else:
						form = ProductImagesForm(request.POST, request.FILES)
						productImage = request.FILES['productImage2']
						form = ProductImages(product = Product.objects.get(id = prodId), productImage=productImage)
						form.save()
				if request.FILES.get('productImage3',False) != False:
					if(count == 3):
						update_img = ProductImages.objects.get(id = imgIds[2])
						update_img.productImage.delete()
						update_img.productImage = request.FILES['productImage3']
						update_img.save()
					else:
						form = ProductImagesForm(request.POST, request.FILES)
						productImage = request.FILES['productImage3']
						form = ProductImages(product = Product.objects.get(id = prodId), productImage=productImage)
						form.save()
				messages.success(request, 'Product record updated!', extra_tags='save')

			elif 'btnDelete' in request.POST:
				prodId = request.POST.get('pprodID')
				delete_product = Product.objects.filter(id = prodId).update(isdeleted = True)
				messages.success(request, 'Product record deleted!', extra_tags='save')

			return redirect('product:index_view')

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
					


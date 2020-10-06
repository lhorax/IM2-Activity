from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.contrib import messages
from product.models import *
from customer.models import *
from product.forms import *
from django.db.models import Count
from django.db.models.functions import TruncMonth

# Create your views here.

class MainIndexView(View):
	def get(self, request):
		qsproducts = Product.objects.all()
		customers = Customer.objects.all()

		for prod in qsproducts:
			prod.ProductImages = ProductImages.objects.filter(product_id = prod.id)

		# Customer chart
		chartCustomer = (Customer.objects.all().
			extra(
				select = {
					'month':"EXTRACT(month FROM date_regis)",
					'year': "EXTRACT(year FROM date_regis)",
				}
			).values('month','year').annotate(count_items = Count('date_regis'))
		)

		# 0 registrants as default for for 12 months 
		valCustomer = [0,0,0,0,0,0,0,0,0,0,0,0]
		totalCustomer = 0
		
		for c in chartCustomer:
			totalCustomer += c['count_items']
			valCustomer[c['month']-1] += c['count_items']

		# Product chart
		chartProduct = (Product.objects.all().
			extra(
				select = {
					'month':"EXTRACT(month FROM dateRegistered)",
					'year': "EXTRACT(year FROM dateRegistered)",
				}
			).values('month','year').annotate(count_items = Count('dateRegistered'))
		)

		# 0 registrants as default for for 12 months 
		valProduct = [0,0,0,0,0,0,0,0,0,0,0,0]
		totalProduct = 0
		
		for c in chartProduct:
			totalProduct += c['count_items']
			valProduct[c['month']-1] += c['count_items']

		context = {
			'products':qsproducts,
			'customers':customers,
			'valCustomer': valCustomer,
			'valProduct': valProduct,
			'totalCustomer': totalCustomer,
			'totalProduct': totalProduct,
		}
		
		return render(request, 'main/dashboard.html',context)

	def post(self,request):
		if(request.method == 'POST'):
			if 'addCustBtn' in request.POST:
				return redirect('customer:registration_view')

			if 'addProdBtn' in request.POST:
				return redirect('product:registration_view')
			
			if 'customerBuy' in request.POST:
				cid = request.POST.get("customer-id")
				request.session['cid'] = cid
				return redirect('buy:index_view')

			if 'btnUpdateCustomer' in request.POST:
				sid = request.POST.get("customer-id")

				fname = request.POST.get("firstname")
				middlename = request.POST.get("middlename")
				lastname = request.POST.get("lastname")
				street = request.POST.get("street")
				brgy = request.POST.get("brgy")
				prov = request.POST.get("prov")
				zp = request.POST.get("zip")
				country = request.POST.get("country")

				birthdate = request.POST.get("birthdate")

				status = request.POST.get("status")
				gender = request.POST.get("gender")
				height = request.POST.get("height")
				weight = request.POST.get("weight")
				religion = request.POST.get("religion")

				sp_name = request.POST.get("spouse-name")
				sp_job = request.POST.get("spouse-occupation")
				children = request.POST.get("no-of-children")
				m_name = request.POST.get("mother-name")
				m_job = request.POST.get("mother-occupation")
				f_name = request.POST.get("father-name")
				f_job = request.POST.get("father-occupation")

				email = request.POST.get("email")
				phone = request.POST.get("phone")

				update_customer = Customer.objects.filter(person_ptr_id = sid).update(firstname = fname, middlename = middlename, lastname = lastname, street = street,
							brgy = brgy, prov = prov, zp = zp, country = country, birthdate = birthdate, status = status,
							gender = gender, height = height, weight = weight, religion = religion, sp_name = sp_name, 
							sp_job = sp_job, children = children, m_name = m_name, m_job = m_job, f_name = f_name, f_job = f_job,
							email = email, phone = phone)
				
				if request.FILES.get("myPhoto",False) != False:
					update_img = Person.objects.get(id = sid)
					if update_img.profile_pic != "placeholder.png":
						update_img.profile_pic.delete()
					update_img.profile_pic = request.FILES['myPhoto']
					update_img.save()
				
				messages.success(request, 'Customer record updated!', extra_tags='save')

			elif 'btnUpdateProduct' in request.POST:
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

			elif 'btnCustDelete' in request.POST:
				sid = request.POST.get("customer-id")

				delete_img = Person.objects.get(id=sid)
				if delete_img.profile_pic != "placeholder.png":
					delete_img.profile_pic.delete()

				customer = Customer.objects.filter(person_ptr_id = sid).delete()
				person = Person.objects.filter(id = sid).delete()

				messages.success(request, 'Customer record deleted!', extra_tags='save')

			elif 'btnProdDelete' in request.POST:
				prodId = request.POST.get('pprodID')
				delete_imgs = ProductImages.objects.filter(product_id = prodId)
				for img in delete_imgs:
					img.delete()
				delete_product = Product.objects.get(id = prodId).delete()
				messages.success(request, 'Product record deleted!', extra_tags='save')

			return redirect('main:index_view')
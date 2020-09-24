from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.contrib import messages
from .forms import CustomerForm
from .models import *

# Create your views here.
class CustomerIndexView(View):
	def get(self, request):
		customers = Customer.objects.all()
		context = {
			'customers':customers
		}
		# print(customers)
		return render(request, 'customer/index.html',context)
	def post(self, request):
		if(request.method == 'POST'):
			if 'addCustBtn' in request.POST:
				return redirect('customer:registration_view')
			if 'btnUpdateCustomer' in request.POST:
				return render(request, 'customer/index.html')
			if 'btnDelete' in request.POST:
				return render(request, 'customer/index.html')
	

class CustomerRegistrationView(View):
	def get(self, request):
		return render(request, 'customer/createCustomer.html')

	def post(self, request):
		form = CustomerForm(request.POST, request.FILES)

		if form.is_valid():
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

			profile_pic = "placeholder.png"
			if request.FILES.get("myPhoto",False) != False:
				profile_pic = request.FILES['myPhoto'] 

			email = request.POST.get("email")
			phone = request.POST.get("phone")

			form = Customer(firstname = fname, middlename = middlename, lastname = lastname, street = street,
							brgy = brgy, prov = prov, zp = zp, country = country, birthdate = birthdate, status = status,
							gender = gender, height = height, weight = weight, religion = religion, sp_name = sp_name, 
							sp_job = sp_job, children = children, m_name = m_name, m_job = m_job, f_name = f_name, f_job = f_job,
							profile_pic = profile_pic, email = email, phone = phone)

			form.save()
			messages.success(request, 'Customer record saved!', extra_tags='save')
			return redirect('customer:registration_view')
		else:
			print(form.errors)
			messages.error(request, 'Error!', extra_tags='error')
			return redirect('customer:registration_view')


from django.shortcuts import render
from django.views.generic import View, TemplateView
from django.http import Http404
from django.http import HttpResponse
from .forms import CustomerForm
from .models import *

# Create your views here.
class CustomerIndexView(View):
	def get(self, request):
		return render(request, 'customer/index.html')
	def post(self, request):
		return render(request, 'customer/createCustomer.html')
	

class CustomerRegistrationView(View):
	def get(self, request):
		return render(request, 'customer/createCustomer.html')
	def post(self, request):
		form = CustomerForm(request.POST, request.FILES)

		if form.is_valid():
			fname = request.POST.get("fname")
			middlename = request.POST.get("mname")
			lastname = request.POST.get("lname")
			street = request.POST.get("street")
			brgy = request.POST.get("barangay")
			prov = request.POST.get("province")
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

			form = Customer(firstname = fname, middlename = middlename, lastname = lastname, street = street,
							brgy = brgy, prov = prov, zp = zp, country = country, birthdate = birthdate, status = status,
							gender = gender, height = height, weigth = weight, religion = religion, sp_name = sp_name, 
							sp_job = sp_job, children = children, m_name = m_name, m_job = m_job, f_name = f_name, f_job = f_job,
							profile_pic = profile_pic)

			form.save()
			return HttpResponse('Success')
		else:
			print(form.errors)
			return HttpResponse('error')


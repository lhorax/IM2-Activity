from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.contrib import messages
from .models import *

# Create your views here.
class LandingIndexView(View):
	def get(self, request):
		return render(request, 'landingpage/LandingPage.html')
	def post(self, request):
		if 'login' in request.POST:
			username = request.POST.get("Username")
			accounts = Admin.objects.filter(username = username)
			if accounts.count() == 0:
				messages.success(request, 'Account does not exist!', extra_tags='valid')
			else:
				password = request.POST.get("Password")
				for account in accounts:
					if account.password == password:
						return redirect('main:index_view')
					else:
						messages.success(request, 'Password does not match', extra_tags='valid')
						break
		return render(request, 'landingpage/LandingPage.html')
	

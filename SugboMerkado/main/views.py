from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView


# Create your views here.

class MainIndexView(View):
	def get(self, request):
		return render(request, 'main/dashboard.html')

	def post(self,request):
		if(request.method == 'POST'):
			if 'addCustBtn' in request.POST:
				return redirect('customer:registration_view')
			if 'addProdBtn' in request.POST:
				return redirect('product:registration_view')
			if 'btnUpdateCustomer' in request.POST:
				return render(request, 'main/dashboard.html')
			if 'btnUpdateProduct' in request.POST:
				return render(request, 'main/dashboard.html')
			if 'btnDelete' in request.POST:
				return render(request, 'main/dashboard.html')
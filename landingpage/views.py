from django.shortcuts import render
from django.views.generic import View, TemplateView
# Create your views here.

class LandingIndexView(View):
	def get(self, request):
		return render(request, 'landingpage/LandingPage.html')
	def post(self, request):
		return render(request, 'landingpage/LandingPage.html')
	

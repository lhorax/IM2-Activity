from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
	path('', views.MainIndexView.as_view(), name="index_view"),
]
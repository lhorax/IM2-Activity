from django.urls import path
from . import views

app_name = 'order'
urlpatterns = [ 
	path('index', views.OrderIndexView.as_view(), name="index_view"),
    path('cart', views.OrderListView.as_view(), name="cart_view"),
    path('bag', views.OrderedProductsView.as_view(), name="bag_view"),
]
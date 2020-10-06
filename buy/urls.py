from django.urls import path
from . import views

app_name = 'buy'
urlpatterns = [ 
    # path('api/data', views.get_data, name='api-data'),
    #TEST URL
    path('index', views.BuyIndexView.as_view(), name="index_view"),
]

from django.urls import path
from . import views

app_name = 'customer'
urlpatterns = [ 
    # path('api/data', views.get_data, name='api-data'),

    #TEST URL
    path('index', views.CustomerIndexView.as_view(), name="index_view"),
    path('registration', views.CustomerRegistrationView.as_view(), name="registration_view"),
]

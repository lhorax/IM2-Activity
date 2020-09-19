from django.urls import path
from . import views

app_name = 'landingpage'
urlpatterns = [ 
    # path('api/data', views.get_data, name='api-data'),

    #TEST URL
    path('', views.LandingIndexView.as_view(), name="landing_view"),
    
]
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


app_name = 'customer'
urlpatterns = [ 
    # path('api/data', views.get_data, name='api-data'),

    #TEST URL
    path('index', views.CustomerIndexView.as_view(), name="index_view"),
    path('registration', views.CustomerRegistrationView.as_view(), name="registration_view"),
]
urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
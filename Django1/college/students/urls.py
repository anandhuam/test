from django.urls import path
from . import views

urlpatterns = [
    path('index',views.index,name='index'),
    path('About_us',views.About_us,name='About'),
    path('Contact',views.Contact,name='Contact'),
    
]

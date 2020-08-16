from django.urls import path
from  .import views
#from . views import Home
from django.shortcuts import render,redirect ,get_object_or_404
from django.contrib.auth.models import User ,auth
from django.contrib import messages
from cart.views import Home, add_to_cart, remove_from_cart
#from django.shortcuts import get_or_create
#from .form import ContactForm
#from .views import Home

app_name ='mainapp'

urlpatterns =[
    path('' ,Home.as_view(),name='home'),
    #path('', views.Home, name='home'),
    path('cart/<slug>', add_to_cart, name='cart'),
    path('remove/<slug>', remove_from_cart, name='remove-cart'),
    
]

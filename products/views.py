from django.shortcuts import render, redirect ,get_object_or_404
from django.views.generic import ListView
from .models import Products 
from django.contrib.auth.models import User ,auth
from django.contrib import messages
#from django.shortcuts import get_or_create
#from .form import ContactForm
#from products.models import Products 

# Create your views here.
#class  Home(ListView):
 #   model = Products
 #   template_name = 'products/home.html'

def Home(request):
    pro = Products.objects.all()

    return render(request ,'products/home.html' ,{'goods' :pro})
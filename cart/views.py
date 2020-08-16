from django.shortcuts import render,redirect ,get_object_or_404
from django.contrib.auth.models import User ,auth
from django.contrib import messages
#from django.shortcuts import get_or_create
#from .form import ContactForm

# Create your views here.

def add_to_cart(request ,slug):
    item = get_objects_or_404(Product , slug=slug)
    order_item , created = Cart.objects.get_or_create(item =item ,user =request.user)

    order_qs =Order.objects.filter(user =request.user , ordered =False)

    if order_qs.exists():
        order =order_qs[0]

        # check if the order item is in the order
        if order.oderitems.filter(item_slug=item.slug).exists():
            order_item.quantity +=1
            order_item.save()
            message.info(request ,'This item quantity was updated.')
            
            return redirect("mainapp :Home")

        else:
            order.oderitems.add(order_item)
            message.info(request ,'This was added to your cart.')
            return redirect("mainapp:Home")

    else:

        order =Order.objects.create(user =request.user) 
        order.oderitems.add(order_item) 
        message.info(request ,"This item was added to your cart.")
        return redirect("mainapp:Home")          



def remove_from_cart(request ,slug):
    item =get_objects_or_404(Product ,slug=slug)
    cart_qs =Cart.objects.filter(user =request.user ,item=item)

    if cart_qs.exists():
        cart =cart_qs[0]

        # Checking the cart quantity
        if cart.quantity > 1:
            cart.quantity -= 1
            cart.save()

        else:
            cart_qs.delete()
            order_qs =Order.objects.filter(user =request.user , ordered=False)


    if order_qs.exists():
        ordered =order_qs[0]

        # check if the order item is in the orde
        if order.oderitems.filter(item_slug =item.slug).exists():
            order_item = Cart.objects.filter(item=item ,user=request.user),[0]
            order.oderitems.remove(order_item)
            message.info(request ,'This item was removed from your cart.')
            return redirect("mainapp:Home")


        else:
            message.info(request ,"This item was not in your cart")
            return redirect("mainapp:Home")


    else:
       message.info(request ,"You do not have an active order")
       return redirect("core:Home")         
















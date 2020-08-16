#from django.db import models
from django.contrib.auth import get_user_model
from products.models import Products
from django.db import models

# Create your models here.
User = get_user_model()

class Cart(models.Model):
    user =models.ForeignKey(User ,on_delete =models.CASCADE)
    item =models.ForeignKey(Products ,on_delete =models.CASCADE)
    quantity =models.IntegerField(default =1)
    Created = models.DateTimeField(auto_now_add =True)
    


    def __str__(self):
        return f' {self.quantity } of {self.item.name}'


class Order(models.Model):
    Orderitems = models.ManyToManyField(Cart)
    user =models.ForeignKey(User ,on_delete=models.CASCADE)
    Ordered = models.BooleanField(default=False)

    Created =models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.username   




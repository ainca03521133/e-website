from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Models):
    user = models.OneToOneField(User, on_delete=models.CASCADE ,null=True, blank=True) 
    #models.CASCDE是使此項資料關聯，一旦刪除，與之關聯的資料都會消失
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200, null= True)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField()
    digital = models.BooleanField(default= False, null=True, blank=False)
    #image
    def __str__(self):
        return(self.name)
    
class Order(models.Modl):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)
    
class OrderItem(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.SET_NULL,blank=True, null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True)
    date_added = models.DateTimeField(auto_now_add=True,)

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,blank=True, null=True)
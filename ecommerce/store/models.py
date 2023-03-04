from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
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
    image = models.ImageField(null=True, blank=True)
    def __str__(self):
        return(self.name)
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ""
            return url
    ###獲取圖片的URL，如果出現異常則返回空字符串。在這裡，self代表當前的Product對象，self.image代表這個對象的圖片屬性。self.image.url返回這個圖片在媒體文件夾中的URL。如果獲取URL過程中出現異常，則返回一個空字符串。

###使用@property裝飾器將這個方法轉換為屬性之後，我們可以直接通過product.imageURL的方式獲取圖片的URL，而不需要再調用一個方法。這樣做的好處是可以讓代碼更加簡潔，而且使用起來更加方便。因此，@property裝飾器在Django中被廣泛使用，特別是在模型中經常被使用。
    
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
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
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    zipcode = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address 
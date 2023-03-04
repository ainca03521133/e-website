from django.shortcuts import render
from .models import *
# Create your views here.
def store(request):
    prodcucts = Product.objects.all()
    #從product這個模組資料庫中的，索取所用物件的用法，fliter(可以設置篩選條件)
    context= {'products':prodcucts}
    return render(request, 'store/store.html',context)

def cart(request):
    context= {}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)


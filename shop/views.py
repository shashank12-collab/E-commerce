from django.http import HttpResponse
from django.shortcuts import render
from shop.models import Product
from math import ceil

# Create your views here.

def index(request):
   allprod = []
   catprods = Product.objects.values('category' , 'id')
   cats = {item['category'] for item in catprods}
   for cat in cats:
       prod = Product.objects.filter(category = cat)
       n = len(prod)
       nslides = n//4 + ceil((n/4) - (n//4))
       allprod.append([prod , range(1 , nslides) , nslides]) 
   prod = {'allprod':allprod}
   return render(request ,'shop/index.html' , prod)   

def about(request):
    return render(request ,'shop/about.html')

def contact(request):
    return render(request ,"shop/contact.html")

def tracker(request):
    return render(request , 'shop/tracker.html')

def search(request):
    return render(request , 'shop/search.html')

def productview(request , id):
    #fetch the product using the id
    product = Product.objects.filter(id = id)
    print(product)
    return render(request ,'shop/product.html' , {'product' : product[0]})

def checkout(request):
    return render(request , 'shop/checkout.html')
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
    return HttpResponse("we are contact")

def tracker(request):
    return HttpResponse("we are tracker")

def search(request):
    return HttpResponse("we are search")

def productview(request):
    return HttpResponse("we are product")

def checkout(request):
    return HttpResponse("we are chaeckout")
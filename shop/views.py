from django.http import HttpResponse
from django.shortcuts import render
from shop.models import Product
from math import ceil

# Create your views here.

def index(request):
    product = Product.objects.all()
    print(product)
    n = len(product)
    nslides = n//4 + ceil((n/4) - (n//4))
    prod = {'no_of_slides':nslides ,'range': range(1 ,nslides) , 'product':product}
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
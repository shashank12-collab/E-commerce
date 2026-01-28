from django.http import HttpResponse
from django.shortcuts import render
from shop.models import Product

# Create your views here.

def index(request):
    product = Product.objects.all()
    return render(request ,'shop/index.html' , {"products" : product})

def about(request):
    return HttpResponse("we are about")

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
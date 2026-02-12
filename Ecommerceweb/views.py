from django.http import HttpResponse
from django.shortcuts import render
from shop.models import Product , Contact 
from shop.models import Orders
from math import ceil

# Create your views here.

def index(request):
   
   return render(request ,'index.html')  
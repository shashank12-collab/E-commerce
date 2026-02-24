from django.http import HttpResponse
from django.shortcuts import render
from blog.models import Blogpost

# Create your views here.

def index(request):

   return render(request ,'index.html')  
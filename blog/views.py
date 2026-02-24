from django.http import HttpResponse
from .models import Blogpost
from django.shortcuts import render

# Create your views here.
def index(request):
    allblog = Blogpost.objects.all()
    return render(request , 'blog/index.html' , {'allblog':allblog})


def blogPost(request , id):
    post = Blogpost.objects.filter(post_id = id)[0]
    return render(request , 'blog/blogPost.html' , {'post':post})



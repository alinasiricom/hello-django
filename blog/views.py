from django.shortcuts import render
from .models import *

def home_view(request):
    posts = Post.objects.filter(status=True)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def single_view(request):
    return render(request, 'blog/blog-single.html')

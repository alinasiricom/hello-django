from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import *

def home_view(request):
    posts = Post.objects.filter(status=1, published_date__lte = timezone.now())
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

def single_view(request, pid):
    post = get_object_or_404(Post, pk=pid, status=1, published_date__lte = timezone.now())
    post.counted_views += 1
    post.save()
    context = {'post':post}
    return render(request, 'blog/blog-single.html', context)

def test_view(request, pid):
    post = get_object_or_404(Post, pk=pid)
    context = {'post':post}
    return render(request, 'blog/test.html', context)

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import *

def home_view(request, cat=None):
    posts = Post.objects.filter(status=1, published_date__lte = timezone.now())
    if cat: posts = posts.filter(category__name = cat)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def single_view(request, pid):
    prev_post = 'none'
    next_post = 'none'
    posts = Post.objects.filter(status=1, published_date__lte = timezone.now())
    si = len(posts)
   
    if si>1:
        for p in range(0, si):
            if posts[p].id == pid:
                if p==0:
                    next_post = posts[1]
                elif p==si-1:
                    prev_post = posts[si-2]
                else:
                    prev_post = posts[p-1]
                    next_post = posts[p+1]
                break
            
    post = get_object_or_404(Post, pk=pid, status=1, published_date__lte = timezone.now())
    post.counted_views += 1
    post.save()
    context = {'post':post, 'prev_post':prev_post, 'next_post':next_post}
    return render(request, 'blog/blog-single.html', context)


def test_view(request, pid):
    post = get_object_or_404(Post, pk=pid)
    context = {'post':post}
    return render(request, 'blog/test.html', context)

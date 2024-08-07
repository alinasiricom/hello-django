from django import template
from blog.models import *
from django.utils import timezone

register = template.Library()

@register.inclusion_tag('blog/blog-latest-posts.html')
def latestposts(n=5):
    posts = Post.objects.filter(status=1, 
        published_date__lte = timezone.now()).order_by('-published_date')[:n]
    return {'posts': posts}

@register.inclusion_tag('blog/blog-posts-categories.html')
def postscategories():
    cats = Category.objects.all()
    posts = Post.objects.filter(status=1, published_date__lte = timezone.now())
    pcats_dict = {}
    
    for c in cats:
        pcats_dict[c] = posts.filter(category=c).count()
    pcats_dict = dict(sorted(pcats_dict.items(), key=lambda x: -x[1]))        # sort dict
    
    return {'pcats': pcats_dict}
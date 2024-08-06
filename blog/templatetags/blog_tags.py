from django import template
from blog.models import *
from django.utils import timezone

register = template.Library()

@register.inclusion_tag('blog/blog-latest-posts.html')
def latestposts(n=5):
    posts = Post.objects.filter(status=1, 
        published_date__lte = timezone.now()).order_by('-published_date')[:n]
    return {'posts': posts}
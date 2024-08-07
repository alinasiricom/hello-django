from django import template
from django.utils import timezone
from blog.models import Post

register = template.Library()

@register.simple_tag(name='lastposts')
def mainapp_lastposts():
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now())[:6]
    return posts
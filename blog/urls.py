from django.urls import path
from .views import *

app_name = 'blog'

urlpatterns = [
    path('', home_view, name='home'),
    path('<int:pid>', single_view, name='single'),
    path('post-<int:pid>', test_view, name='test'),
]
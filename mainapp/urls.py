from django.urls import path
from .views import *

app_name = 'mainapp'

urlpatterns = [
    path('maintenance/', maintenance_view, name='maintenance'),
    path('', index_view, name='index'),
    path('about', about_view, name='about'),
    path('contact', contact_view, name='contact'),
    path('test', test_view, name='test'),
    path('newsletter', newsletter_view, name='newsletter'),
]
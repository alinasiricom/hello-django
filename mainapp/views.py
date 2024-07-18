from django.shortcuts import render

def index_view(request):
    return render(request, 'mainapp/index.html')

def about_view(request):
    return render(request, 'mainapp/about.html')

def contact_view(request):
    return render(request, 'mainapp/contact.html')
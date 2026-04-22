from django.shortcuts import render
from .models import Settings, Service
# Create your views here.

def geeks(request):
    return render(request, 'geeks.html')

def index(request):
    return render(request, 'index.html')
def blog(request):
    return render(request, 'blog.html')
def blog_single(request):
    return render(request, 'blog-single.html')
def page_404(request):
    return render(request, '404.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contacts(request):
    return render(request, 'contacts.html')
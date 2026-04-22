from django.shortcuts import render
from .models import Settings, Service
# Create your views here.

def geeks(request):
    return render(request, 'geeks.html')

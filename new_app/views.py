from django.shortcuts import render
from .models import *

def home(request):
    return render(request, 'includes/index.html')

def contact(request):
    return render(request, 'includes/contact.html')

def single(request):
    return render(request, 'includes/single.html')

def category(request):
    return render(request, 'includes/category.html')

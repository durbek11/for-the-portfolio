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

def signup(request):
    form = Registration()
    if request.method == "POST":
        form = Registration(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    
    return render(request, 'registration/signup.html', {"form":form})

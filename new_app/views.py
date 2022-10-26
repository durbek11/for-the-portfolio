from django.shortcuts import render
from .models import *
from .form import *

def home(request):
    context = {
        "date": date, 
         "products":products,
    }
    return render(request, 'includes/index.html', context)
    
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
            return redirect('/Login/')
    
    return render(request, 'registration/signup.html', {"form":form})




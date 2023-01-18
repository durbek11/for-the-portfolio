from itertools import product
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views import generic
from .form import *
from django.db.models import Q
from django.http import JsonResponse


def home(request):
   date = Date.objects.all()

   context = {
        "date": date,
    }
   return render(request, 'includes/index.html', context)

def arrivals_detail(request, pk):
    arrivals_detalis = Arrival.objects.get(id=pk)

    context ={
        "arrivals_detalis":arrivals_detalis
    }

    return render(request, "includes/cat.html", context)
    
def contact(request):
    return render(request, 'includes/contact.html')

def single(request):
    
    return render(request, "includes/single.html")

def cat(request):
    category = request.GET.get('category')
    if category == None:
        arrivals = Arrival.objects.all()
    else:
        arrivals = Arrival.objects.filter(category__category_name=category)
    
    categires = Category.objects.all()
    context = {
        "arrivals":arrivals,
        "categoryes":categires,
    }
    return render(request, "includes/cat.html", context)
   

    

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




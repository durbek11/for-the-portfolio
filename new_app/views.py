from django.shortcuts import render
from .models import *

def home(request):
    return render(request, 'pages/home.html')

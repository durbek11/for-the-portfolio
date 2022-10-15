from django.urls import path
from .views import *

app_name = 'NEWSROOM'

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact')
]

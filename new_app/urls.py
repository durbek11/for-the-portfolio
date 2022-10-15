from django.urls import path
from .views import *

app_name = 'new_project'

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact')
]

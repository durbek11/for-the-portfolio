from django.urls import path
from django.contrib.auth.views import LoginView , LogoutView
from .views import *

from rest_framework import views

app_name = 'NEWSROOM'

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('single/',  single, name='single'),
    path('category/', category, name='category'),
    path('Login/', LoginView.as_view(), name='Login'),
    path('signup/', signup, name='signup'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('help/<slug:slug>/', views.post_detail, name='post_detail')
]

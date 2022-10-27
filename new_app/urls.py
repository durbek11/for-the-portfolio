from django.urls import path
from django.contrib.auth.views import LoginView , LogoutView
from .views import *

app_name = 'NEWSROOM'

urlpatterns = [
    path('', home, name='home'),
    path('contact/', contact, name='contact'),
    path('single/',  single, name='single'),
    path('category/', category, name='category'),
    path('Login/', LoginView.as_view(), name='Login'),
    path('signup/', signup, name='signup'),
       path('logout/', LogoutView.as_view(), name="logout"),
]

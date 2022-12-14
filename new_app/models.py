from audioop import add
from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.utils.timezone import datetime
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse

class MyUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    is_organiser = models.BooleanField(default=False)
    is_agent = models.BooleanField(default=False)

class Date(models.Model):
    date1 = models.TextField(max_length=70)

    def __str__(self):
        return self.date1

class Contact(models.Model):
    TAKLIF = "Taklif"
    SHIKOYAT = "Shikoyat"
    CONTACT_CHOICES = [
        (TAKLIF, "Taklif"),
        (SHIKOYAT, "Shikoyat")
    ]
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    choices = models.CharField(max_length=8, choices=CONTACT_CHOICES, default=TAKLIF)
    mobile = models.IntegerField(default=9989)
    message = models.TextField(max_length=700)
    date = models.DateTimeField(auto_now=add)
    def __str__(self):
        return self.choices

class Arrival(models.Model):
    arrivals_img = models.ImageField()
    arrivals_title = models.CharField(max_length=200)
    arrivals_price = models.IntegerField(default=10)
    category = models.ForeignKey("Category", blank=True, on_delete=models.CASCADE)

    #asosiy ma`lumotlar uchun
    arrivals_size  = models.CharField(max_length=30)
    arrivals_text = models.TextField(max_length=700)
    
    def __str__(self):
        return self.arrivals_title

class Category(models.Model):
    class Meta:
        verbose_name = 'My Category'
        verbose_name_plural = 'My Categorys'
        
    category_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.category_name

    

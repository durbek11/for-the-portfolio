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

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField(default=1, null=True, blank=True)
    img = models.ImageField(upload_to="images/")
    score = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )

    def __str__(self):
        return str(f"id:{self.pk} score:{self.score} title:{self.title}")

class Comment(models.Model):
    post = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='comments')
    authour = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    message = models.CharField(max_length=50)
    rate_product = models.IntegerField(default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(f"post author - {self.authour}")
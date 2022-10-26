from django.contrib import admin
from .models import *

admin.site.register(MyUser)
admin.site.register(Date)
admin.site.register(Product)
admin.site.register(Comment)

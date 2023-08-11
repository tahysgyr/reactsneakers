from django.contrib import admin
from .models import Products, Images,Cart

# Register your models here.

admin.site.register(Products)
admin.site.register(Images)
admin.site.register(Cart)
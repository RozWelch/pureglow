from django.contrib import admin
from .models import Product, SkinCategory

# Register your models here.
admin.site.register(Product)
admin.site.register(SkinCategory)
from django.contrib import admin
from .models import Product, SkinCategory

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'product_size',
        'price',
        'star_rating',
        'is_new',
        'image',
    )

    ordering = ('sku',)


class SkinCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(SkinCategory, SkinCategoryAdmin)

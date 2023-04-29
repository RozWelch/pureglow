from django.contrib import admin
from wishlist.models import Wishlist


class WishlistAdmin(admin.ModelAdmin):
    list_display = (
        'user_profile',
        'product',
    )

    ordering = ('-user_profile',)


admin.site.register(Wishlist, WishlistAdmin)
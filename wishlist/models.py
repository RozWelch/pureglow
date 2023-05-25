from django.db import models
from profiles.models import UserProfile
from products.models import Product


class Wishlist(models.Model):
    """ Wish list Model """
    user_profile = models.ForeignKey(UserProfile, null=True, blank=True,
                                     on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=True, blank=True,
                                on_delete=models.CASCADE, default=1)

    def __str__(self):
        """ String representation of the Wishlist Model """
        return f'Wishlist ({self.user_profile})'

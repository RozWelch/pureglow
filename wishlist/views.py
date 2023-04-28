from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.conf import settings
from django.contrib import messages

from profiles.models import UserProfile
from products.models import Product
from wishlist.models import Wishlist


def wishlist(request):
    """ The view to show a logged in user's wish list """
    if not request.user.is_authenticated:
        messages.error(request,
                       'Please log in to view your wish list')
        return redirect(reverse('account_login'))

    user = get_object_or_404(UserProfile, user=request.user)
    wishlist = Wishlist.objects.filter(user_profile=user)

    template = 'wishlist/wishlist.html'

    context = {
        'wishlist': wishlist,
    }

    return render(request, template, context)


def add_to_wishlist(request, product_id):
    """
    The view to add a product to a logged in user's wishlist
    and prevent them from adding products that are already
    on the user's wishlist
    """
    if not request.user.is_authenticated:
        messages.error(request,
                       'Please log in to view your wish list')
        return redirect(reverse('account_login'))

    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)

    # checks if product is already on a user's wishlist
    existing = Wishlist.objects.filter(product=product,
                                       user_profile=user).exists()
    if existing:
        messages.info(request, f'{product.name} is already on your wishlist.')
        return redirect(reverse('product_detail', args=[product.id]))
    else:
        wishlist_item = Wishlist.objects.create(user_profile=user,
                                                product=product)
    messages.success(request,
                     f'{product.name} has been added to your wishlist.')

    return redirect(reverse('product_detail', args=[product.id]))


def remove_from_wishlist(request, product_id):
    """ A view to remove a product from a user's wishlist """
    if not request.user.is_authenticated:
        messages.error(request,
                       'Please log in to view your wish list')
        return redirect(reverse('account_login'))

    user = get_object_or_404(UserProfile, user=request.user)
    product = get_object_or_404(Product, pk=product_id)
    Wishlist.objects.filter(product=product,
                            user_profile=user).delete()
    messages.info(request,
                  f'{product.name} is removed from your wishlist.')

    return redirect(reverse('product_detail', args=[product.id]))

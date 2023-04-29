from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Model for reviews
class Reviews(models.Model):

    product = (models.ForeignKey(
        Product, on_delete=models.CASCADE,
        related_name="product_reviews")
        )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    content = models.TextField(max_length=400)
    date_created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    star_rating = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return f"Review {self.review} by {self.name}"

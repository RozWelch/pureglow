from django.db import models
from django.contrib.auth.models import User


class HowTo(models.Model):
    article_title = models.CharField(max_length=210, unique=True)
    slug = models.SlugField(max_length=210, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="article_posts")
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)    
    created_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='article_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.article_title        

    def number_of_likes(self):
        return self.likes.count()

class ArticleComment(models.Model):
    post = models.ForeignKey(HowTo, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    comment_body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']
    
    def __str__(self):
        return f"Comment {self.comment_body} by {self.name}"
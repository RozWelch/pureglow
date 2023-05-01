from django.shortcuts import render
from django.views import generic
from .models import HowTo, ArticleComment


class HowToList (generic.ListView):
    model = HowTo
    template_name = "articles.html"
    paginate_by = 6

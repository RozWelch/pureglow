from django.shortcuts import render
from django.views import generic
from .models import HowTo, ArticleComment


class HowToList (generic.ListView):
    model = HowTo
    queryset = order_by('-created_on')
    template_name = articles.html
    paginate_by = 6
    

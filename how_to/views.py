from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic, View
from .models import HowTo, ArticleComment


class HowToList(generic.ListView):
    model = HowTo
    template_name = "articles.html"


def howto_detail(request, slug):
    """ A view to show how to articles """

    howto = get_object_or_404(HowTo, slug=slug)

    context = {
        'howto': howto,
    }

    return render(request, 'articles_detail.html', context)


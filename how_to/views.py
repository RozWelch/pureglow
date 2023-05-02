from django.shortcuts import render
from django.views import generic, View
from .models import HowTo, ArticleComment


class HowToList(generic.ListView):
    model = HowTo
    template_name = "articles.html"
    paginate_by = 6


def howto_detail(request, product_id):
    """ A view to show full how to article """

    article = get_object_or_404(HowTo, slug=slug)

    context = {
        'howto': howto,
    }

    return render(request, 'how_to/articles_detail.html', context)
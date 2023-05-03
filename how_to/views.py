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


# class HowToDetail(View):

#     def get(self, request, slug, *args, **kwargs):
#         queryset = HowTo.objects
#         post = get_object_or_404(queryset, slug=slug)
#         comments = post.comments.filter(approved=True).order_by("-created_on")
#         liked = False
#         if post.likes.filter(id=self.request.user.id).exists():
#             liked = True

#         return render(
#             request,
#             "articles_detail.html",
#             {
#                 "post": post,
#                 "comments": comments,
#                 "liked": liked
#             },
#         )

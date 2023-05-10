from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic, View
from .models import HowTo, ArticleComment
from .forms import ArticleCommentForm
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin


class HowToList(generic.ListView):
    model = HowTo
    template_name = "articles.html"


# def howto_detail(request, slug):
#     """ A view to show how to articles """

#     howto = get_object_or_404(HowTo, slug=slug)

#     context = {
#         'howto': howto,
#     }

#     return render(request, 'articles_detail.html', context)



class HowToDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = HowTo.objects
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")

        return render(
            request,
            "articles_detail.html",
            {
                "post": post,
                "comments": comments,
                "comment_form": ArticleCommentForm()
            },
        )
    
    def post(self, request, slug, *args, **kwargs):

        queryset = HowTo.objects
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")

        comment_form = ArticleCommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = ArticleCommentForm()

        return render(
            request,
            "articles_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": ArticleCommentForm()
            },
        )
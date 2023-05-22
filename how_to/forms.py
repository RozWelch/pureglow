from .models import ArticleComment, HowTo
from django import forms


class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = ArticleComment
        fields = ('comment_body',)


class ArticleForm(forms.ModelForm):
    class Meta:
        model = HowTo
        fields = ('article_title', 'content', 'image')

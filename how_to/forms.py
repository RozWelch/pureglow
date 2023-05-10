from .models import ArticleComment
from django import forms


class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = ArticleComment
        fields = ('comment_body',)
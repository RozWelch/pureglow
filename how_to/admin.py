from django.contrib import admin
from .models import HowTo, ArticleComment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(HowTo)
class HowToAdmin(SummernoteModelAdmin):

    list_display = ('article_title', 'slug', 'created_on')
    search_fields = ['article_title', 'content']
    list_filter = ('article_title', 'created_on')
    prepopulated_fields = {'slug': ('article_title',)}
    summernote_fields = ('content',)


@admin.register(ArticleComment)
class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment_body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'comment_body')
    actions = ['approve_comments']

    def approve_articlecomments(self, request, queryset):
        queryset.update(approved=True)

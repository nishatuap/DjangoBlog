from django.contrib import admin

# Register your models here.
from articles.models import Article, Comment

'''class CommentInline (admin.StackedInline):  #stacked = representation objet / tabular = representation database table
    model = Comment'''
class CommentInline (admin.TabularInline):
    model = Comment
class ArticleAdmin (admin.ModelAdmin):
    inlines = [
        CommentInline
    ]
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
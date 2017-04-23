from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    fields = ['title', 'content']
    list_display = ('title', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['title']

admin.site.register(Article, ArticleAdmin)

from django.contrib import admin
from .models import Topic, Article

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'published_at')
    list_filter = ('topic', 'published_at')
    search_fields = ('title', 'summary')

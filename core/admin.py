from django.contrib import admin

from .models import Article, Topic


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "topic", "source_name", "published_at", "image_url")
    list_filter = ("topic", "published_at", "source_name")
    search_fields = ("title", "summary", "source_name", "image_url")

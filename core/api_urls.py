from django.urls import path

from .api_views import ArticleListView, TopicListView, health

urlpatterns = [
    path("health/", health),
    path("topics/", TopicListView.as_view(), name="api-topics"),
    path("articles/", ArticleListView.as_view(), name="api-articles"),
]

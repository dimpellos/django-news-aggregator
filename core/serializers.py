from rest_framework import serializers
from .models import Topic, Article

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ["id", "name", "slug"]

class ArticleSerializer(serializers.ModelSerializer):
    topic = TopicSerializer(read_only=True)

    class Meta:
        model = Article
        fields = ["id", "title", "url", "summary", "published_at", "source_name", "topic"]

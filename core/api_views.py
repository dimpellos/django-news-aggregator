from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db.models import Q
from .models import Topic, Article
from .serializers import TopicSerializer, ArticleSerializer

class TopicListView(ListAPIView):
    queryset = Topic.objects.all().order_by("name")
    serializer_class = TopicSerializer

class ArticleListView(ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        qs = Article.objects.select_related("topic").order_by("-published_at")
        topic = self.request.query_params.get("topic")
        q = self.request.query_params.get("q")
        if topic:  # accept slug or id
            qs = qs.filter(Q(topic__slug=topic) | Q(topic_id=topic))
        if q:
            qs = qs.filter(Q(title__icontains=q) | Q(summary__icontains=q))
        return qs

@api_view(["GET"])
def health(request):
    return Response({"status": "ok"})

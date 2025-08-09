from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Article, Topic


def home(request):
    topics = Topic.objects.all().order_by("name")
    qs = Article.objects.select_related("topic").order_by("-published_at")

    topic_id = request.GET.get("topic")
    if topic_id:
        qs = qs.filter(topic_id=topic_id)

    q = request.GET.get("q")
    if q:
        qs = qs.filter(Q(title__icontains=q) | Q(summary__icontains=q))

    paginator = Paginator(qs, 12)
    page = request.GET.get("page")
    articles = paginator.get_page(page)

    return render(
        request,
        "core/home.html",
        {
            "topics": topics,
            "articles": articles,
        },
    )


def topic_detail(request, slug):
    topics = Topic.objects.all().order_by("name")
    topic = get_object_or_404(Topic, slug=slug)

    qs = Article.objects.filter(topic=topic).order_by("-published_at")

    q = request.GET.get("q")
    if q:
        qs = qs.filter(Q(title__icontains=q) | Q(summary__icontains=q))

    paginator = Paginator(qs, 12)
    articles = paginator.get_page(request.GET.get("page"))

    return render(
        request,
        "core/topic_detail.html",
        {
            "topics": topics,
            "topic": topic,
            "articles": articles,
        },
    )

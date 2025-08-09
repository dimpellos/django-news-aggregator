from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Topic, Article

def home(request):
    topics = Topic.objects.all().order_by('name')

    qs = Article.objects.select_related('topic').order_by('-published_at')

    topic_id = request.GET.get('topic')
    if topic_id:
        qs = qs.filter(topic_id=topic_id)

    q = request.GET.get('q')
    if q:
        qs = qs.filter(title__icontains=q) | qs.filter(summary__icontains=q)

    paginator = Paginator(qs, 12)  # 12 cards per page
    page = request.GET.get('page')
    articles = paginator.get_page(page)

    return render(request, 'core/home.html', {
        'topics': topics,
        'articles': articles,
    })

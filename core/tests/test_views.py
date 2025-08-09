import pytest
from django.urls import reverse
from django.utils import timezone

from core.models import Article, Topic


@pytest.mark.django_db
def test_home_lists_articles(client):
    topic = Topic.objects.create(name="Tech")
    Article.objects.create(
        topic=topic,
        title="AI news",
        url="https://e/x",
        summary="...",
        published_at=timezone.now(),
    )
    resp = client.get(reverse("home"))
    assert resp.status_code == 200
    assert "AI news" in resp.content.decode()


@pytest.mark.django_db
def test_home_search_filters(client):
    t = Topic.objects.create(name="Tech")
    Article.objects.create(
        topic=t,
        title="Python",
        url="https://e/1",
        summary="py",
        published_at=timezone.now(),
    )
    Article.objects.create(
        topic=t,
        title="Football",
        url="https://e/2",
        summary="sport",
        published_at=timezone.now(),
    )
    resp = client.get(reverse("home"), {"q": "Python"})
    html = resp.content.decode()
    assert "Python" in html and "Football" not in html

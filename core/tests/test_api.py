import pytest
from django.urls import reverse
from django.utils import timezone

from core.models import Article, Topic


@pytest.mark.django_db
def test_api_articles_list(client):
    t = Topic.objects.create(name="Tech")
    Article.objects.create(
        topic=t,
        title="Item",
        url="https://e/x",
        summary="",
        published_at=timezone.now(),
    )
    resp = client.get(reverse("api-articles"))  # ensure your name matches
    assert resp.status_code == 200
    data = resp.json()
    assert data["count"] >= 1

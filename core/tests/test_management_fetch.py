from unittest.mock import patch

import pytest
from django.core.management import call_command

from core.models import Article, Topic


@pytest.mark.django_db
@patch("core.management.commands.fetch_articles.requests.get")
def test_fetch_articles_adds_items(mock_get, settings):
    settings.NEWSAPI_KEY = "dummy"
    Topic.objects.create(name="Business")
    mock_get.return_value.json.return_value = {
        "status": "ok",
        "articles": [
            {
                "title": "Hello",
                "url": "https://example.com/hello",
                "description": "desc",
                "publishedAt": "2025-08-01T12:00:00Z",
                "urlToImage": "https://example.com/img.jpg",
                "source": {"name": "Example"},
            }
        ],
    }
    call_command("fetch_articles")
    assert Article.objects.filter(url="https://example.com/hello").exists()

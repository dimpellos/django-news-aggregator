import pytest
from django.utils import timezone

from core.models import Article, Topic


@pytest.fixture
def topic():
    return Topic.objects.create(name="Business")


@pytest.fixture
def article(topic):
    return Article.objects.create(
        topic=topic,
        title="Sample",
        url="https://example.com/a",
        summary="s",
        published_at=timezone.now(),
        source_name="Example",
        image_url="",
    )

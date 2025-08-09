import pytest

from core.models import Topic


@pytest.mark.django_db
def test_topic_slug_autofills():
    t = Topic.objects.create(name="My Cool Topic")
    assert t.slug == "my-cool-topic"

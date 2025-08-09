import factory
from django.utils import timezone

from core.models import Article, Topic


class TopicFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Topic

    name = factory.Sequence(lambda n: f"Topic {n}")


class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article

    topic = factory.SubFactory(TopicFactory)
    title = factory.Sequence(lambda n: f"Article {n}")
    url = factory.Sequence(lambda n: f"https://example.com/{n}")
    summary = "Summary"
    published_at = factory.LazyFunction(timezone.now)
    source_name = "Source"
    image_url = ""

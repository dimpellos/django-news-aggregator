import requests
from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_datetime
from django.utils.timezone import is_naive, make_aware

from core.models import Article, Topic


class Command(BaseCommand):
    help = "Fetches articles from NewsAPI and saves them to the database"

    def handle(self, *args, **options):
        api_key = settings.NEWSAPI_KEY
        url = "https://newsapi.org/v2/everything"

        topics = Topic.objects.all()
        if not topics:
            self.stdout.write(self.style.WARNING("No topics found. Add some via the admin panel."))
            return

        for topic in topics:
            params = {
                "q": topic.name,
                "apiKey": api_key,
                "language": "en",
                "pageSize": 5,
                "sortBy": "publishedAt",
            }

            response = requests.get(url, params=params)
            data = response.json()

            if data.get("status") != "ok":
                self.stdout.write(
                    self.style.ERROR(f"Failed to fetch articles for topic: {topic.name}")
                )
                continue

            for article_data in data.get("articles", []):
                raw_date = article_data["publishedAt"]
                published_at = parse_datetime(raw_date)

                if published_at and is_naive(published_at):
                    published_at = make_aware(published_at)

                source_name = ""
                src = article_data.get("source")
                if isinstance(src, dict):
                    source_name = src.get("name") or ""

                # Extract image URL
                image_url = article_data.get("urlToImage") or ""

                article, created = Article.objects.get_or_create(
                    url=article_data["url"],
                    defaults={
                        "topic": topic,
                        "title": (article_data.get("title") or "")[:255],
                        "summary": article_data.get("description") or "",
                        "published_at": published_at,
                        "source_name": source_name,
                        "image_url": image_url,  # ← make sure this is here
                    },
                )

                if created:
                    self.stdout.write(self.style.SUCCESS(f"Added article: {article.title}"))
                else:
                    self.stdout.write(f"Skipped existing article: {article.title}")

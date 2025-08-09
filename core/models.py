from django.db import models
from django.utils.text import slugify

class Topic(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Article(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)  # enforce no duplicates across topics
    summary = models.TextField(blank=True)
    published_at = models.DateTimeField()
    source_name = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        indexes = [
            models.Index(fields=['-published_at']),
        ]

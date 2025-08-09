from django.db import models

class Topic(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=255)
    url = models.URLField()
    summary = models.TextField(blank=True)
    published_at = models.DateTimeField()

    def __str__(self):
        return self.title

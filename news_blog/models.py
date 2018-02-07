from django.db import models
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField(default=timezone.now)
    text = models.TextField()
    published_date = models.DateTimeField(
        blank=True, null=True)

# Create your models here.

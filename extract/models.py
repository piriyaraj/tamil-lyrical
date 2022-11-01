from email.policy import default
from enum import unique
from django.db import models

# Create your models here.
class ExtractData(models.Model):
    lastSitemap = models.URLField(max_length = 200)
    lastPost=models.URLField(max_length=200)

class PostUrls(models.Model):
    url=models.URLField(max_length=1000,unique=True)
    status=models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.url

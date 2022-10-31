from django.db import models

# Create your models here.
class ExtractData(models.Model):
    lastSitemap = models.URLField(max_length = 200)
    lastPost=models.URLField(max_length=200)
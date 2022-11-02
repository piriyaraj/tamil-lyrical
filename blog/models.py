from django.urls import reverse
from urllib.request import Request, urlopen
from tempfile import NamedTemporaryFile
from django.core.files import File
from enum import unique
from pickletools import unicodestring1
from pyexpat import model
from django.db import models
from django.utils.text import slugify

class Song(models.Model):
    title = models.CharField(max_length=100)
    songe=models.CharField(max_length=10000)
    songt=models.CharField(max_length=10000)
    created=models.DateField(auto_now_add=True)
    slug=models.SlugField(unique=True)
    movie = models.ForeignKey(
        'Movie', on_delete=models.CASCADE, blank=True, null=True)
    singer = models.ManyToManyField('Singer', blank=True)
    composer = models.ForeignKey(
        'Composer', on_delete=models.CASCADE, blank=True, null=True)
    lyricist = models.ForeignKey(
        "Lyricist", on_delete=models.CASCADE, blank=True, null=True)


    def get_absolute_url(self):
        return reverse("lyrics", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Movie(models.Model):
    name = models.CharField(max_length=1000)
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add= True)
    year = models.IntegerField(blank=True)
    imgUrl = models.URLField(max_length=1000, blank=True)
    imageThumb=models.ImageField(upload_to="movieThumb")
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("movie", args=[self.slug])

    def save(self, *args, **kwargs):
        if self.imgUrl and not self.imageThumb:
            req = Request(
                url=self.imgUrl,
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            img_temp = NamedTemporaryFile(delete=True)
            img_temp.write(urlopen(req).read())
            img_temp.flush()
            self.imageThumb.save(f"image_{self.name}", File(img_temp))
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Singer(models.Model):
    name = models.CharField(max_length=1000)
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("singer", args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Composer(models.Model):
    name = models.CharField(max_length=1000)
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("composer", args=[self.slug])

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Lyricist(models.Model):
    name = models.CharField(max_length=1000)
    slug = models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse("lyricist", args=[self.slug])

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

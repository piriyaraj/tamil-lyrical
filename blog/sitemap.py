from unittest import result
from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse
from .models import  Composer, Lyricist, Movie, Singer, Song


class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['index']

    def location(self, item):
        return reverse(item)


class LyricsSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Song.objects.all()


class MovieSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Movie.objects.all()


class ComposerSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Composer.objects.all()


class SingerSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Singer.objects.all()


class LyricistSitemap(Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Lyricist.objects.all()

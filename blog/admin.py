

from django.contrib import admin

from .models import *

@admin.register(Song)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    # search_fields = ('content', )

    prepopulated_fields = {'slug': ('title', )}


@admin.register(Movie)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    # search_fields = ('content', )

    prepopulated_fields = {'slug': ('name', )}

@admin.register(Singer)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    # search_fields = ('content', )

    prepopulated_fields = {'slug': ('name', )}


@admin.register(Lyricist)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    # search_fields = ('content', )

    prepopulated_fields = {'slug': ('name', )}

@admin.register(Composer)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    # search_fields = ('content', )

    prepopulated_fields = {'slug': ('name', )}

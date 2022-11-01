from django.contrib import admin

from extract.models import ExtractData, PostUrls

# Register your models here.


admin.site.register(ExtractData)


@admin.register(PostUrls)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('url', 'status')
    # search_fields = ('content', )

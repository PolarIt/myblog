from django.contrib import admin
from article.models import Article
from article.models import Tag

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title',  'date_time')
    search_fields = ('title', 'tags', 'tag_name', 'content')
    list_filter = ("date_time",)
    filter_horizontal = ('tags',)
    date_hierarchy = 'date_time'

class TagAdmin(admin.ModelAdmin):
	list_display = ('tag_name',)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag,TagAdmin)
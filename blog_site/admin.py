from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'body', 'date_pubs')
    search_fields = ('title', 'body')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title',)

# admin.site.register(Post)

'''Imports'''
from django.contrib import admin
from frights.models import MoviePost, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(MoviePost)
class MoviePostAdmin(SummernoteModelAdmin):
    '''Registers Movie Posts to admin'''
    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('summary',)

# Register your models here.
admin.site.register(Comment)

from django.contrib import admin
from .models import Movie, Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Movie)
class MoviePostAdmin(SummernoteModelAdmin):
    '''Registers Movie Posts to admin'''
    list_display = ('title', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('summary',)
    def __str__(self):
        return self.title

# Register your models here.
admin.site.register(Comment)

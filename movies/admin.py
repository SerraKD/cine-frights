from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Movie, Comment, RecommendMovie


@admin.register(Movie)
class MoviePostAdmin(SummernoteModelAdmin):
    """
    Registers Movie Posts to admin
    """
    list_display = ('title', 'slug', 'status')
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('summary',)


admin.site.register(Comment)


@admin.register(RecommendMovie)
class RecommendMovieAdmin(admin.ModelAdmin):
    """
    Registers movie recommendations to admin
    """

    list_display = ('movie_title', 'additional_comments', 'read',)
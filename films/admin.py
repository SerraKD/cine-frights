from django.contrib import admin
from movies.models import Movie, Comment
from .models import NewsLetter
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
admin.site.register(NewsLetter)

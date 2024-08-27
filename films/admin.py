from django.contrib import admin
from movies.models import Movie, Comment
from .models import Member, Newsletter
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
admin.site.register(Member)
admin.site.register(Newsletter)

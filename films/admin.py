from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from movies.models import Movie, Comment
from .models import Member, Newsletter


admin.site.register(Member)
admin.site.register(Newsletter)

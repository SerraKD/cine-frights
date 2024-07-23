'''Imports'''
from django.contrib import admin
from frights.models import MoviePost, Comment

# Register your models here.
admin.site.register(MoviePost)
admin.site.register(Comment)

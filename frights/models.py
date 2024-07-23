'''Imports'''
from django.db import models
from django.contrib.auth.models import User

POST_STATUS = ((0, "Not Published"), (1, "Published"))

# Create your models here.

class MoviePosts(models.Model):
    '''Class for movie posts '''
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="movie_posts"
)
    # Add images with claudinary
    summary = models.TextField(blank=False, null=False, default="text")
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=POST_STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    excerpt = models.TextField(blank=True)
    imdb_rating = models.IntegerField(blank=False, null=False, default=0)
    rotten_tomatoes_rating = models.IntegerField(blank=False, null=False, default=0)
    # Add our ratings

'''Imports'''
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

POST_STATUS = ((0, "Not Published"), (1, "Published"))


class Movie(models.Model):
    """
    Class for movie posts.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="movie_posts")
    movie_poster = CloudinaryField('image', default='placeholder')
    release_date = models.SlugField(
        blank=False, null=False, default=0, max_length=4)
    summary = models.TextField(blank=False, null=False, default="text")
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=POST_STATUS, default=0)
    updated_on = models.DateTimeField(auto_now=True)
    excerpt = models.TextField(blank=True)
    imdb_rating = models.TextField(
        blank=False, null=False, max_length=3, default="0")
    rotten_tomatoes_rating = models.TextField(
        blank=False, null=False, max_length=3, default="0")
    our_rating = models.TextField(
        blank=False, null=False,  max_length=26, default="0")

    class Meta:
        '''
        A meta class for meta data, posts are listed from newest to oldest
        '''
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    """
    Class for user comments comment on a movie post.
    """
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name="movie_comments")
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="movie_comments")
    content = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        '''
        A meta class for meta data, comments are listed from newest to oldest
        '''
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.content} | by {self.username}"


class RecommendMovie(models.Model):
    """
    Class representing movie recommendation from user.
    """
    username = models.CharField(max_length=200)
    email = models.EmailField()
    movie_title = models.TextField(max_length=200)
    additional_comments = models.TextField(max_length=200)
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Movie recommendation from {self.username}"

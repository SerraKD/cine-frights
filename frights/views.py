from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from frights.models import MoviePost, Comment

# Create your views here.
class HomePageView(generic.ListView):
    queryset = MoviePost.objects.filter(status=1)
    template_name = "home.html"

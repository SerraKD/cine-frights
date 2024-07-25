from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Movie, Comment

# Create your views here.
class HomePageView(generic.ListView):
    queryset = Movie.objects.filter(status=1)
    template_name = "movies/index.html"
    paginate_by = 4
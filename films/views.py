from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from movies.models import Movie, Comment


# Create your views here.
class FilmsPageView(generic.ListView):
    ''' Method to movie post corousel'''
    queryset = Movie.objects.filter(status=1)
    template_name = "films/films.html"

def MovieDetailView(request, slug):
    ''' to display selected movie post details'''
    queryset = Movie.objects.filter(status=1)
    movie = get_object_or_404(queryset, slug=slug)

    return render(
    request,
    "movies/movie_detail.html",
    {
        "movie": movie,
    },
)
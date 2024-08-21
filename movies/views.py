from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import Movie, Comment

# Create your views here.
class HomePageView(generic.ListView):
    ''' Method to display all movie posts'''
    queryset = Movie.objects.filter(status=1)
    template_name = "movies/index.html"

def MovieDetailView(request, slug):
    ''' to display selected movie post details'''
    queryset = Movie.objects.filter(status=1)
    movie = get_object_or_404(queryset, slug=slug)
    comments = Comment.objects.all().order_by("-created_on")
    comment_count = Comment.objects.filter(approved=True).count()
    movie.movie_comments.filter(approved=True).count()

    return render(
    request,
    "movies/movie_detail.html",
    {
        "movie": movie,
        "comments": comments,
        "comment_count": comment_count,
    },
)

    

    

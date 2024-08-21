from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from django.contrib import messages
from .models import Movie, Comment
from .forms import CommentForm

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
    
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.username = request.user
            comment.post = movie
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted, awaiting approval'
    )

    comment_form = CommentForm()

    return render(
    request,
    "movies/movie_detail.html",
    {
        "movie": movie,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
    },
)

    

    

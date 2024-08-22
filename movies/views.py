from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
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
    comments = movie.movie_comments.all().order_by("-created_on")
    comment_count = movie.movie_comments.filter(approved=True).count()
    movie.movie_comments.filter(approved=True).count()
    
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.username = request.user
            comment.movie = movie
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your comment is successfully submitted, will appear after approval'
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

def comment_edit(request, slug, comment_id):
    """
    view to edit movie comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        movie = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.username == request.user:
            comment = comment_form.save(commit=False)
            comment.movie = movie
            comment.approved = False
            comment.save()
            messages.add_message(request, messages.SUCCESS, 'Yor comment is updated.')
        else:
            messages.add_message(request, messages.ERROR, 'An error occured while updating comment, try again.')

    return HttpResponseRedirect(reverse('movie_detail', args=[slug]))


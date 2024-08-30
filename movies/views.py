from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Movie, Comment, RecommendMovie
from .forms import CommentForm, RecommendMovieForm


class HomePageView(generic.ListView):
    """
    View to display all movie posts on the homepage.
    """
    queryset = Movie.objects.filter(status=1)
    template_name = "movies/index.html"


def MovieDetailView(request, slug):
    """
    View to display selected movie post details.
    """
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
                """Your comment is successfully submitted,
                 it will appear after approval."""
            )
        else:
            messages.add_message(
                request, messages.ERROR,
                'Something went wrong, please try again.'
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


def recommend_view(request):
    """
    View to display recommend movie form.
    """

    if request.method == "POST":
        recommend_movie_form = RecommendMovieForm(data=request.POST)
        if recommend_movie_form.is_valid():
            recommend_movie_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                """Thank you,we recieved your recommendation.
                You will get an respond within a week."""
            )
        else:
            messages.add_message(
                request, messages.ERROR,
                """Something went wrong, please try again."""
            )

    recommend_movie_form = RecommendMovieForm()

    return render(
        request,
        "movies/recommend_movie.html",
        {
            "recommend_movie_form": recommend_movie_form
        },
    )


def comment_edit(request, slug, comment_id):
    """
    View to edit movie comments.
    """
    if request.method == "POST":

        queryset = Movie.objects.filter(status=1)
        movie = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.username == request.user:
            comment = comment_form.save(commit=False)
            comment.movie = movie
            comment.approved = False
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your comment is updated.'
            )
        else:
            messages.add_message(
                request, messages.ERROR,
                'An error occured while updating comment, try again.'
            )

    return HttpResponseRedirect(reverse('movie_detail', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    View to delete movie comments.
    """
    queryset = Movie.objects.filter(status=1)
    movie = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.username == request.user:
        comment.delete()
        messages.add_message(
            request, messages.SUCCESS, 'Comment deleted.'
        )
    else:
        messages.add_message(
            request, messages.ERROR,
            'You can only delete your own comments.'
        )

    return HttpResponseRedirect(reverse('movie_detail', args=[slug]))

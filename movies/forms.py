from .models import Comment, RecommendMovie
from django import forms


class CommentForm(forms.ModelForm):
    ''' Movie comment field'''
    class Meta:
        model = Comment
        fields = ('content',)


class RecommendMovieForm(forms.ModelForm):
    ''' Recommend a movie field'''
    class Meta:
        model = RecommendMovie
        fields = ('username', 'email', 'movie_title', 'additional_comments')
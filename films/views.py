from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.contrib import messages
from movies.models import Movie, Comment
from .models import NewsLetter
from .forms import NewsLetterForm


class FilmsPageView(generic.ListView):
    ''' Method to movie post corousel'''
    queryset = Movie.objects.filter(status=1)
    template_name = "films/films.html"
    paginate_by = 3


def NewsLetterView(request):
    '''to display newsletter form'''
    if request.method == "POST":
        newsletter_form = NewsLetterForm(data=request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'You have succesfully subscribed to our Newsletter'
            )
        else:
            messages.add_message(
                request, messages.SUCCESS,
                'You have already subscribed to newsletter with this email.'
    )

    newsletter_form = NewsLetterForm()
    
    return render(
        request,
        "films/newsletter.html",
        {
            "newsletter_form": newsletter_form
        },
    )
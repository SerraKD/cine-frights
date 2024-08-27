from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.contrib import messages
from movies.models import Movie, Comment
from .models import Member
from .forms import MemberForm


class FilmsPageView(generic.ListView):
    ''' Method to movie post corousel'''
    queryset = Movie.objects.filter(status=1)
    template_name = "films/films.html"
    paginate_by = 3


def MembersView(request):
    '''to display join the newsletter form'''
    if request.method == "POST":
        member_form = MemberForm(data=request.POST)
        if member_form .is_valid():
            member_form .save()
            messages.add_message(
                request, messages.SUCCESS,
                'You have succesfully subscribed to our Newsletter'
            )
        else:
            messages.add_message(
                request, messages.SUCCESS,
                'You have already subscribed to newsletter with this email.'
    )

    member_form = MemberForm()
    
    return render(
        request,
        "films/newsletter.html",
        {
            "member_form": member_form
        },
    )

def Remove(request):
    '''to display unsubscribe the newsletter form'''
    remove = Member.objects.get(data=request.GET)
    if request.method == "GET":
        remove.delete()
        messages.add_message(
            request, messages.SUCCESS,
            'You have succesfully unsubscribed to our Newsletter'
        )
    else:
        messages.add_message(
            request, messages.SUCCESS,
            'You have already unsubscribed to newsletter with this email.'
        )

    
    return render(
        request,
        "films/newsletter.html",
    )
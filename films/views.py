from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
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
                'You have already subscribed to newsletter with this email.')

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
    if request.method == "POST":
        email = request.POST.get("email")
        if email:
            try:
                # valid email
                member = Member.objects.get(email=email)
                member.delete()
            except Member.DoesNotExist:
                messages.add_message(
                    request, messages.ERROR,
                    'This email adress is not subscribed to the newsletter.')
            else:
                # let user know that they unsubscribed succesfully
                messages.add_message(
                    request, messages.SUCCESS,
                    'You have succesfully unsubscribed to our Newsletter')

        else:
            # not valid
            messages.add_message(
                request, messages.ERROR,
                'Request failed, please check the email provided.'
            )
    member_form = MemberForm()

    return HttpResponseRedirect(reverse('news_letter'))
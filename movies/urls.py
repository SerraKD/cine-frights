'''Imports'''
from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('<slug:slug>/', views.MovieDetailView, name='movie_detail'),
]
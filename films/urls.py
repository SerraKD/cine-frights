from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePageView.as_view(), name='films'),
    path('<slug:slug>/', views.MovieDetailView, name='movie_detail'),
]
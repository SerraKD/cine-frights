from . import views
from django.urls import path

urlpatterns = [
    path('', views.FilmsPageView.as_view(), name='films'),
    path('newsletter/', views.NewsLetterView, name='news_letter'),
]
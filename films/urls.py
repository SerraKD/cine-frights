from . import views
from django.urls import path

urlpatterns = [
    path('', views.FilmsPageView.as_view(), name='films'),
    path('newsletter/', views.MembersView, name='news_letter'),
    path('unsubscribe/', views.Remove, name='unsubscribe'),
]
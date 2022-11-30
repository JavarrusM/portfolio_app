from django.urls import path
from . import views

app_name = 'tmdb_movie_barchart'

urlpatterns = [
    path('', views.home, name='tmdb_movie_barchart'),
]
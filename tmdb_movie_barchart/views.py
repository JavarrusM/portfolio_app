from django.shortcuts import render

# Create your views here.
def home(request):
    return(render(request, 'tmdb_movie_barchart/index.html'))

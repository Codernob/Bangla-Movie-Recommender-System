from django.shortcuts import render
from .models import Movie,Cast,Director,Genre
# Create your views here.

def home(request):
    return render(request,'home.html',{})

def movies(request):
    return render(request,'movies.html',{
        "movies":Movie.objects.all()
    })

def genres(request):
    return render(request,'genres.html',{
        "genres":Genre.objects.all()
    })

def celebrities(request):
    return render(request,'celebrities.html',{
        "celebrities":Cast.objects.all()
    })

def movie(request, movie_id):
    movieo = Movie.objects.get(id=movie_id)
    return render(request, "movie.html", {
        "movie": movieo
    })

def celebrity(request, celebrity_id):
    celebrityo = Cast.objects.get(id=celebrity_id)
    return render(request, "celebrity.html", {
        "celebrity": celebrityo
    })
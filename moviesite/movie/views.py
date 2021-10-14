from django.shortcuts import render
from .models import Movie,Cast,Director
# Create your views here.

def home(request):
    return render(request,'home.html',{})

def movies(request):
    return render(request,'movies.html',{
        "movies":Movie.objects.all()
    })

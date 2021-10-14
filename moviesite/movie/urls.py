from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('movies.html',views.movies,name="movies")
]

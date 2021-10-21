from django.urls import path
from . import views

urlpatterns = [
    path('home.html',views.home,name="home"),
    path('movies.html',views.movies,name="movies"),
    path('genres.html',views.genres,name="genres"),
    path('celebrities.html',views.celebrities,name='celebrities'),
    path("<int:movie_id>", views.movie, name="movie"),
]

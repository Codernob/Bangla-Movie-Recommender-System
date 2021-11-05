from django.urls import path
from django.urls.conf import include
from . import views
# from django.contrib.auth.views import LoginView
# from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('home.html',views.home,name="home"),
    path('movies.html',views.movies,name="movies"),
    path('genres.html',views.genres,name="genres"),
    path('celebrities.html',views.celebrities,name='celebrities'),
    path("celebrities/<int:celebrity_id>", views.celebrity, name="celebrity"),
    path("movies/<int:movie_id>", views.movie, name="movie"),
    path('searchresult.html',views.search,name="searchresult"),
    path('login.html',views.login,name='login'),
    path('signup.html',views.signup,name='signup'), 
    path('logout',views.logout,name='logout'),
    
]

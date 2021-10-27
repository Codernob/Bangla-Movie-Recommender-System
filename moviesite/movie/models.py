from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=64)
    release_date = models.DateField(null=True, blank=True)
    overview = models.CharField(max_length=10000, default='Not Updated Yet')
    celebrities = models.ManyToManyField("Cast", blank=True, related_name="movie_celeb")
    def __str__(self):
        return f"{self.title}"

class Genre(models.Model):
    genre_name = models.CharField(max_length=20)
    movies = models.ManyToManyField(Movie, blank=True, related_name="movie_genre")
    def __str__(self):
        which_movie = ", ".join(str(seg) for seg in self.movies.all())
        return f"The genre of {which_movie} is {self.genre_name}"

Genders = (
    ('MALE','Male'),
    ('FEMALE','Female'),
    ('OTHER','Other'))

class Cast(models.Model):
    name = models.CharField(max_length=64)
    gender = models.CharField(max_length=6, choices=Genders, default='Male')
    date_of_birth = models.DateField(null=True, blank=True)
    overview = models.CharField(max_length=1000, default='Not Updated Yet')
    biography = models.CharField(max_length=10000, default='Not Updated Yet')
    movies = models.ManyToManyField(Movie, blank=True, related_name="cast_movie")
    def __str__(self):
        which_movie = ", ".join(str(seg) for seg in self.movies.all())
        return f"{self.name} acted in {which_movie}"

class Director(models.Model):
    name = models.CharField(max_length=64)
    gender = models.CharField(max_length=6, choices=Genders, default='Male')
    date_of_birth = models.DateField(null=True, blank=True)
    which_movie = models.ForeignKey(Movie, on_delete=models.SET_NULL, blank=True, null=True)
    def __str__(self):
        return f"{self.name} directed {self.which_movie}"

class Subscriber(models.Model):
    name = models.CharField(max_length=64)
    gender = models.CharField(max_length=6, choices=Genders, default='Male')
    date_of_birth = models.DateField(null=True, blank=True)
    movie = models.ManyToManyField(Movie, blank=True, related_name="user_movie", through='Rate')
    email=models.CharField(max_length=30,null=True, blank=True)
    password=models.CharField(max_length=20,null=True)

    def __str__(self):
        return f"{self.name} {self.email} {self.gender}"

class Rate(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    rating = models.IntegerField()
    def __str__(self):
        return f"{self.user} rates {self.movie} a {self.rating}"

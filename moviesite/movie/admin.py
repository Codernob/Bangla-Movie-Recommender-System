from django.contrib import admin
from .models import Movie,Genre,Cast,Director,Subscriber,Rate

# Register your models here.
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(Cast)
admin.site.register(Director)
admin.site.register(Subscriber)
admin.site.register(Rate)
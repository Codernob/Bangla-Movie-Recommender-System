from django.shortcuts import redirect,HttpResponse ,render
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Genders,Movie,Cast,Director,Genre
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

def search(request):
    # if request.method == "POST":
    searched = request.POST['searched']
    movie_re = Movie.objects.filter(title__contains=searched)
    return render(request,'searchresult.html', {'movie_re':movie_re})

def login(request):  
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')        
    else:
        return render(request,'layout.html')     

def signup(request):
    if request.method== 'POST':
        username=request.POST['username']
        email=request.POST['email']
        date_of_birth=request.POST['date_of_birth']
        #gender=request.POST['gender']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            user=User.objects.create_user(username=username,email=email,date_of_birth=date_of_birth,pasasword=password1)
            user.save();
            return redirect('login') 
        #print('User created')
        return redirect('/')
    # else:
    return render(request,'layout.html')     
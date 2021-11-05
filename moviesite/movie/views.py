from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect,HttpResponse,render
from django.contrib import messages
from django.contrib.auth.models import User,auth
from .models import Genders,Subscriber,Movie,Cast,Director,Genre
from django.contrib.auth import logout as django_logout

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
        password1=request.POST['password1']
        
        user=auth.authenticate(username=username,password=password1)

        # if user is not None:
        if user is not None or Subscriber.objects.filter(password=password1).exists():    
            auth.login(request,user)
            #messages.error(request,'Login Successful') 
            return redirect('home.html')
            
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login.html')        
    else:
        return render(request,'login.html')     

def signup(request):
    if request.method== 'POST':
        username=request.POST['username']
        email=request.POST['email']
        date_of_birth=request.POST['date_of_birth']
        gender=request.POST['gender']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
            user=Subscriber(name=username,email=email,date_of_birth=date_of_birth,gender=gender,password=password1)
            user.save()
            return render(request,'home.html')     
        #print('User created')
        return redirect('/')
    # else:
    return render(request,'signup.html') 

def profile(request):
    return render(request,'profile.html',{})

def logout(request):
    django_logout(request)
    return  HttpResponseRedirect('home.html')
    # auth.logout(request)
    # return redirect('/')
    #if request.method == 'POST':
    # logout(request)
    # return redirect('/')   
    #return HttpResponseRedirect('home.html')
    
    
    

 
    
    #Git fol.
from django.shortcuts import render
from .models import Review
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages 
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, authenticate, logout 



# Create your views here.

def index(request):
    return render(request, 'reviews/index.html', {
        'page_name': 'index'
    })


def movie1(request):
    review = Review.objects.all()
    review_count = review.count()
    if request.method == "POST":
        print(request.POST)
        movie1 = Review.objects.create(
            user_name=request.POST.get('user_name'),
            comment=request.POST.get('comment'),
            rating=request.POST.get('Rating')
        )
        movie1.save()
        context ={
            'reviews': review,
            'count': review_count,
            'page_name': 'movie1',
        }
        return render(request, 'reviews/movie1.html', context)
    else:
         review = Review.objects.all()
    review_count = review.count()
    context = {
        'reviews': review,
        'count': review_count,
        'page_name': 'movie1',
    }
    return render(request, 'reviews/movie1.html', context)

def movie2(request):
    review = Review.objects.all()
    review_count = review.count()
    if request.method == "POST":
        print(request.POST)
        movie1 = Review.objects.create(
            user_name=request.POST.get('user_name'),
            comment=request.POST.get('comment'),
            rating=request.POST.get('Rating')
        )
        movie2.save()
        context ={
            'reviews': review,
            'count': review_count,
            'page_name': 'movie1',
        }
        return render(request, 'reviews/movie1.html', context)
    else:
         review = Review.objects.all()
    review_count = review.count()
    context = {
        'reviews': review,
        'count': review_count,
        'page_name': 'movie2',
    }
    return render(request, 'reviews/movie2.html', context)


def movie3(request):
    review = Review.objects.all()
    review_count = review.count()
    if request.method == "POST":
        print(request.POST)
        movie1 = Review.objects.create(
            user_name=request.POST.get('user_name'),
            comment=request.POST.get('comment'),
            rating=request.POST.get('Rating')
        )
        movie3.save()
        context ={
            'reviews': review,
            'count': review_count,
            'page_name': 'movie3',
        }
        return render(request, 'reviews/movie3.html', context)
    else:
         review = Review.objects.all()
    review_count = review.count()
    context = {
        'reviews': review,
        'count': review_count,
        'page_name': 'movie3',
    }
    return render(request, 'reviews/movie3.html', context)

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm
	return render (request=request, template_name="reviews/register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="reviews/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")
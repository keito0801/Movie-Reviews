from django.shortcuts import render
from .models import Review

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
            user_name=request.user.username,
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
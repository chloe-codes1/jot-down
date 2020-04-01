from django.shortcuts import render, redirect
from .models import Review

# Create your views here.

def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, 'community/review_list.html', context)

def new_review(request):
    return render(request, 'community/new_review.html')


def create_review(request):
    review = Review()
    review.title = request.GET.get('title')
    review.content = request.GET.get('content')
    review.rank = request.GET.get('rank')
    review.save()
    
    return redirect('/community/')

def review_detail(request, pk):
    review = Review.objects.get(id=pk)
    context = {
        'review':review
    }
    return render(request,'community/review_detail.html', context)
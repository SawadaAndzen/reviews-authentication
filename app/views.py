from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Review
from .forms import ReviewForm, CustomUserCreationForm


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'registration/signup.html', {'form': form})


def review_list(request):
    reviews = Review.objects.all().order_by('-pub_date')
    
    return render(request, "review_list.html", {'reviews': reviews})


@login_required
def add_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        
        if form.is_valid():
            review = form.save(commit = False)
            review.author = request.user
            review.save()
            
            return redirect('review_list')
        else:
            form = ReviewForm()
            
        return render(request, "add_review.html", {'form': form})
            
    else:
        form = ReviewForm()
        
        return render(request, "add_review.html", {'form': form})
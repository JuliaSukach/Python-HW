from datetime import datetime

from django.http import HttpResponse

from .models import User
from .models import Post
from django.shortcuts import render, redirect
from django.template import loader
from .utils import get_user
from .utils import paginate
from .forms import PostForm


def main(request):
    user_profile = User.objects.first()
    comments = Post.objects.all()
    form = PostForm(request.POST or None)
    if request.method == "POST":
        form = PostForm(request.POST or None)
        print(form.is_valid())
        if form.is_valid():
            print("it's valid!!")
            post = form.save(commit=False)
            post.username = request.user
            post.save()
            return redirect("main:home")
    context = {
        'user_profile': user_profile,
        'comments': comments,
        "form": form,
        'navbar': 'home',
        'tabs': ['Home', 'Goals', 'Check-In', 'Mail', 'Profile', 'Friends', 'Settings']
    }

    return render(request, "home.html", context)


def food(request):
    return render(
        request,
        "food.html",
        {
            'navbar': 'food',
            'tabs': ['Food Diary', 'Database', 'My Foods', 'My Meals', 'Recipes', 'Settings']
         }
    )


def exercise(request):
    return render(
        request,
        "exercise.html",
        {
            'navbar': 'exercise',
            'tabs': ['Exercise Diary', 'Database', 'My Exercises', 'Settings']
        }
    )


def reports(request):
    return render(
        request,
        "reports.html",
        {
            'navbar': 'reports',
            'tabs': ['home', 'goals', 'check-in', 'mail']
        }
    )


def about(request):
    return render(
        request,
        "about.html",
        {
            'title': "About",
            'content': "About Page"
        }
    )


def contact(request):
    return render(
        request,
        "contact.html",
        {
            'title': "Contact",
            'content': "Contact Page"
        }
    )

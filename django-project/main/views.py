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
            return redirect("main:profile")
    context = {
        'user_profile': user_profile,
        'comments': comments,
        "form": form
    }

    return render(request, "profile.html", context)


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

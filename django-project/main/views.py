from datetime import datetime

from django.shortcuts import render


def main(request):
    now = datetime.now()

    return render(
        request,
        "index.html",
        {
            'content': "Hello Django" + now.strftime("%A, %d %B, %Y at %X")
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

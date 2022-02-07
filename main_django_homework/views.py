import random

from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from blog.models import Comment
numbers = ("067", "096", "097", "098", "050", "066", "095", "099", "050", "066", "095", "099")
random_slug = ["first", "second", "third"]


def homepage(request: HttpRequest) -> HttpResponse:
    my_randint = random.randint(1, 10)
    my_randslug = random.choice(random_slug)
    context = {"homepage": "Main",
               "randint": my_randint,
               "randslug": my_randslug}
    return render(request, "base.html", context)


def articles(request: HttpRequest) -> HttpResponse:
    context = {
        "articles": "Articles"
    }
    return render(request, "articles.html", context)


def archive_a(request: HttpRequest) -> HttpResponse:
    return render(request, "archive_articles.html")


def users(request: HttpRequest) -> HttpResponse:
    return render(request, "users.html")


def view_comments(request: HttpRequest) -> HttpResponse:
    order_by = Comment.objects.order_by("updated_published").order_by("-user_name")[:2]
    comments = Comment.objects.all()
    context = {
        "comments": list(comments)[-5:],
        "ordered": order_by
    }
    for item in Comment.objects.all():
        if "k" in item.comment and "c" not in item.comment:
            item.delete()
    return render(request, "comments.html", context)


def users_num(request: HttpRequest, user_num: int) -> HttpResponse:
    return HttpResponse(f"User number: {user_num}")


def article_int(request: HttpRequest, article_num: int) -> HttpResponse:
    context = {"number": article_num}
    return render(request, "article_num.html", context)


def article_in_archive(request: HttpRequest, article_num: int) -> HttpResponse:
    return HttpResponse(f"<h1>Your article number: {article_num} in  archive</h1>")


def article_slug(request: HttpRequest, article_num: int, slug_text: str) -> HttpResponse:
    context = {"number": article_num,
               "my_slug": slug_text}
    return render(request, "article_num.html", context)


def re_url(request: HttpRequest, url: str) -> HttpResponse:
    return HttpResponse(f"<h1>Your some url: {url}</h1>")


def phone(request: HttpRequest, **kwargs: str) -> HttpResponse:
    if kwargs.get("phone").startswith(numbers):
        return HttpResponse("<h1>Your phone number is valid</h1>")
    else:
        return HttpResponse("<h1>Your number is invalid")

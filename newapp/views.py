from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

numbers = ("067", "096", "097", "098", "050", "066", "095", "099", "050", "066", "095", "099")


def homepage(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Main</h1>"
                        """<ul>
                        <li><a href=http://127.0.0.1:8000/articles/><h2>Articles</h2></li>
                        <li><a href=http://127.0.0.1:8000/users/><h2>Users</h2></li>
                        </ul>""")


def articles(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Articles</h1>"
                        """<h2><a href=http://127.0.0.1:8000/article/1/>Article - 1</h2>"""
                        )


def archive_a(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Archive Articles</h1>")


def users(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>All Users</h1>")


def users_num(request: HttpRequest, user_num: int) -> HttpResponse:
    return HttpResponse(f"User number: {user_num}")


def article_int(request: HttpRequest, article_num: int) -> HttpResponse:
    return HttpResponse(f"<h1>Your article number: {article_num}</h1>")


def article_in_archive(request: HttpRequest, article_num: int) -> HttpResponse:
    return HttpResponse(f"<h1>Your article number: {article_num} in  archive</h1>")


def article_slug(request: HttpRequest, article_num: int, slug_text: str) -> HttpResponse:
    return HttpResponse(f"""<h1>Your article number: {article_num}</h1>
    <h1>Your slug-text: {slug_text}</h1>""")


def re_url(request: HttpRequest, url: str) -> HttpResponse:
    return HttpResponse(f"<h1>Your some url: {url}</h1>")


def phone(request: HttpRequest, **kwargs: str) -> HttpResponse:
    if kwargs.get("phone").startswith(numbers):
        return HttpResponse("<h1>Your phone number is valid</h1>")
    else:
        return HttpResponse("<h1>Your number is invalid")

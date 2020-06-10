from django.shortcuts import render, HttpResponse
from .models import Author, Article, Category
# Create your views here.


def index(request):
    post = Article.objects.all()
    context = {
        "post": post
    }
    return render(request, "index.html", context)


def getAuthor(request, name):
    return render(request, "profile.html")


def getSingle(request, id):
    return render(request, "single.html")


def getTopic(request, name):
    return render(request, "category.html")
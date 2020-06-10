from django.shortcuts import render, HttpResponse, get_object_or_404
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
    post = get_object_or_404(Article, pk=id)
    first = Article.objects.first()
    last = Article.objects.last()
    related = Article.objects.filter(category=post.category).exclude(id=id)[:4]
    context = {
        "post": post,
        "first": first,
        "last": last,
        "related": related
    }
    return render(request, "single.html", context)


def getTopic(request, name):
    cat = get_object_or_404(Category, name=name)
    post = Article.objects.filter(category=cat.id)
    return render(request, "category.html", {"post": post})

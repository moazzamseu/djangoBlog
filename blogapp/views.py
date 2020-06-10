from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Author, Article, Category
from django.contrib.auth import authenticate, login, logout
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


def getLogin(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == "POST":
            user = request.POST.get('user')
            password = request.POST.get('pass')
            auth = authenticate(request, username=user, password=password)
            if auth is not None:
                login(request, auth)
                return redirect('index')
    return render(request, "login.html")


def getLogout(request):
    logout(request)
    return redirect('index')
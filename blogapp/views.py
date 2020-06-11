from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Author, Article, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import createForm, registerUser, createAuthor
from django.contrib import messages

# Create your views here.


def index(request):
    post = Article.objects.all()
    search = request.GET.get('query')
    if search:
        post = post.filter(
            Q(title__icontains=search)|
            Q(body__icontains=search)
        )
    paginator = Paginator(post, 4)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    total_article = paginator.get_page(page_number)
    context = {
        "post": total_article
    }
    return render(request, "index.html", context)


def getAuthor(request, name):
    postAuthor = get_object_or_404(User, username=name)
    auth = get_object_or_404(Author, name=postAuthor.id)
    post = Article.objects.filter(author=auth.id)
    paginator = Paginator(post, 4)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    total_article = paginator.get_page(page_number)
    context = {
        "auth": auth,
        "post": total_article
    }
    return render(request, "profile.html", context)


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
    paginator = Paginator(post, 4)  # Show 25 contacts per page.

    page_number = request.GET.get('page')
    total_article = paginator.get_page(page_number)
    return render(request, "category.html", {"post": total_article, "cat": cat})


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
            else:
                messages.add_message(request, messages.ERROR, 'Username or password mismatch')
    return render(request, "login.html")


def getLogout(request):
    logout(request)
    return redirect('index')


def getCreate(request):
    if request.user.is_authenticated:
        u = get_object_or_404(Author, name=request.user.id)
        form = createForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = u
            instance.save()
            return redirect('index')
        return render(request, 'create.html', {"form":form})
    else:
        return redirect('login')


def getUpdate(request, pid):
    if request.user.is_authenticated:
        u = get_object_or_404(Author, name=request.user.id)
        post = get_object_or_404(Article, id=pid)
        form = createForm(request.POST or None, request.FILES or None, instance=post)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = u
            instance.save()
            messages.success(request, 'Article updated succefully')
            return redirect('profile')
        return render(request, 'create.html', {"form": form})
    else:
        return redirect('login')


def getDelete(request, pid):
    if request.user.is_authenticated:
        post = get_object_or_404(Article, id=pid)
        post.delete()
        messages.warning(request, 'Article is deleted successfully')
        return redirect('profile')
    else:
        return redirect('login')


def getProfile(request):
    if request.user.is_authenticated:
        user = get_object_or_404(User, id=request.user.id)
        author_profile = Author.objects.filter(name=user.id)
        if author_profile:
            authorUser = get_object_or_404(Author, name=request.user.id)
            post = Article.objects.filter(author=authorUser.id)
            return render(request, 'logged_in_profile.html', {"post": post, "user": authorUser})
        else:
            form = createAuthor(request.POST or None, request.FILES or None)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.name = user
                instance.save()
                return redirect('profile')
            return render(request, 'create.html', {"form": form})
    else:
        return redirect('login')


def get_register(request):
    form = registerUser(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Registration successfully completed')
        return redirect('login')
    return render(request, 'register.html', {"form": form})

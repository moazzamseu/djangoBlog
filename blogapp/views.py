from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, "index.html")


def getAuthor(request, name):
    return render(request, "profile.html")

def getSingle(request, id):
    return render(request, "single.html")
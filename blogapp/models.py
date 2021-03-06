from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Author(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    profilePicture = models.FileField()
    details = models.TextField()

    def __str__(self):
        return self.name.username


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField()
    image = models.FileField()
    postedOn = models.DateTimeField(auto_now=False, auto_now_add=True)
    updatedOn = models.DateTimeField(auto_now=True, auto_now_add=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class comment(models.Model):
    post = models.ForeignKey(Article, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    post_comment = models.TextField()

    def __str__(self):
        return self.post.title

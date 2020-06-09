from django.contrib import admin
from .models import Author, Article, Category
# Register your models here.

class authorModel(admin.ModelAdmin):
    list_display = ["__str__", "name"]
    search_fields = ["__str__", "details"]

    class Meta:
        Model = Author
admin.site.register(Author, authorModel)


class articleModel(admin.ModelAdmin):
    list_display = ["__str__", "author", "postedOn"]
    search_fields = ["__str__", "details"]
    list_per_page = 10
    list_filter = ["postedOn", "category"]

    class Meta:
        Model = Article
admin.site.register(Article, articleModel)

class categoryModel(admin.ModelAdmin):
    list_display = ["__str__", "name"]

    class Meta:
        Model = Category
admin.site.register(Category, categoryModel)
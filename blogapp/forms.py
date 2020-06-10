from django import forms
from .models import Article


class createForm(forms.ModelForm):
    class Meta:
        model = Article
        fields=[
            'author',
            'title',
            'body',
            'image',
            'category',
        ]
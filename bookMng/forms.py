import select

from django import forms
from django.forms import ModelForm
from .models import Book
from .models import Comment
from .models import Rating


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'name',
            'web',
            'price',
            'picture',
        ]


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'body'
        ]
        labels = {
            'body': ''
        }


CHOICES = {(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')}
CHOICES = sorted(CHOICES)


class RatingForm(ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']
        labels = {'rating': ''}
        widgets = {'rating': forms.RadioSelect(choices=CHOICES)}

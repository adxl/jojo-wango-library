from django import forms
from django.forms import ModelForm

from books.models import Book, Genre

field_class = "bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"


class BookForm(ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={"class": field_class}),
        label="Nom du livre",
        max_length=64,
    )
    author = forms.CharField(
        widget=forms.TextInput(attrs={"class": field_class}),
        label="Auteur",
        max_length=64,
    )
    editor = forms.CharField(
        widget=forms.TextInput(attrs={"class": field_class}),
        label="Éditeur",
        max_length=64,
    )
    collection = forms.CharField(
        widget=forms.TextInput(attrs={"class": field_class}),
        label="Collection",
        max_length=64,
    )
    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
    class Meta:
        model = Book
        fields = ["title", "author", "editor", "collection", "genres"]


class GenreForm(ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={"class": field_class}),
        label="Intitulé du genre",
        max_length=30,
    )

    class Meta:
        model = Genre
        fields = ["name"]

from django.shortcuts import redirect, render

from books.forms import BookForm, GenreForm
from books.models import Book, Genre


def index_books(request):
    books: list[Book] = Book.objects.order_by("title")
    context: dict[str, any] = {
        "books": books,
    }
    return render(request, "books/index_books.html", context)


def index_genres(request):
    genres: list[Genre] = Genre.objects.order_by("name")
    context: dict[str, any] = {
        "genres": genres,
    }
    return render(request, "books/index_genres.html", context)


def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/books/")

    else:
        form = BookForm()

    return render(
        request,
        "../templates/books/addBook.html",
        {"form": form},
    )


def add_genre(request):
    if request.method == "POST":
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/books/genres/")

    else:
        form = GenreForm()

    return render(
        request,
        "../templates/books/addGenre.html",
        {"form": form},
    )

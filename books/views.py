from django.shortcuts import redirect, render
import logging

from books.forms import BookForm, GenreForm
from books.models import Book, Genre
from forums.models import create_forum, get_forum_by_id

logger = logging.getLogger(__name__)

def index_books(request):
    books: list[Book] = Book.objects.order_by("title")
    # get forum id for each book
    for book in books:
        book.forum_id = get_forum_by_id(book.id)

    logging.warning(books)
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
            create_forum(form.instance.id)
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

from django.urls import include, path  # type: ignore

from books.views import index_books, index_genres, add_book, add_genre

urlpatterns = [
    path("books/", index_books, name="index_books"),
    path("books/genres/", index_genres, name="index_genres"),
    path("books/add/", add_book, name="add_book"),
    path("books/genres/add/", add_genre, name="add_genre"),
]

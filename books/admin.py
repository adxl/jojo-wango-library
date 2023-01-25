from django.contrib import admin
from books.models import Genre, Book

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Genre._meta.local_fields]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Book._meta.local_fields]



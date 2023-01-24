from django.contrib import admin
from books.models import Genre

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Genre._meta.local_fields]



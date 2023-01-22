from django.contrib import admin

from .models import Library, LibraryHasBook

admin.site.register(Library)
admin.site.register(LibraryHasBook)

# Register your models here.

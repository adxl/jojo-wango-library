from django.contrib import admin

from libraries.models import Library, LibraryHasBook


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Library._meta.local_fields]

@admin.register(LibraryHasBook)
class LibraryAdmin(admin.ModelAdmin):
    list_display = [f.name for f in LibraryHasBook._meta.local_fields]

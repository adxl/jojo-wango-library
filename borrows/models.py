import uuid

from django.db import models

from books.models import Book
from libraries.models import Library


class Borrow(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.CASCADE)
    borrowed_at = models.DateTimeField()
    return_at = models.DateTimeField()
    returned_at = models.DateTimeField()

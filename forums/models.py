import uuid
# import logging

# logger = logging.getLogger(__name__)

from django.db import models

from books.models import Book


class Forum(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.TextField()
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

def create_forum(book_id : uuid.UUID) -> uuid.UUID:
    forum = Forum(book_id=book_id)
    forum.save()
    return forum.id

def get_forum_by_id(book_id : uuid.UUID) -> Forum:
    return Forum.objects.get(book_id=book_id)
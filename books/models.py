import uuid

from django.db import models


class Genre(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"



class Book(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    editor = models.CharField(max_length=64)
    collection = models.CharField(max_length=64)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return f"{self.title}"



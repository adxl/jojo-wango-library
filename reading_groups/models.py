from django.db import models

import uuid

from libraries.models import Library

class ReadingGroup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    library = models.ForeignKey(Library, on_delete=models.CASCADE)


class ReadingGroupHasUser(models.Model):
    group = models.ForeignKey(ReadingGroup, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

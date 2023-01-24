from django.db import models
from django.contrib.auth.models import User
import uuid

from libraries.models import Library

class ReadingGroup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()
    library = models.ForeignKey(Library, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.start_at} -> {self.end_at} : {self.library}"


class ReadingGroupHasUser(models.Model):
    group = models.ForeignKey(ReadingGroup, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} in {self.group}"

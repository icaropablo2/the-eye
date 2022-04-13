from email.policy import default
from uuid import uuid4

from django.db import models


class Event(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4)
    session_id = models.UUIDField()
    category = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    data = models.TextField()
    timestamp = models.DateTimeField()

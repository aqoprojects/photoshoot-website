from django.db import models
import uuid

class Service(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    title = models.CharField(max_length=100, null=True, blank=True)
    info = models.TextField(max_length=300, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
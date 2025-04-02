from django.db import models
import uuid 

class Visitor(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    ip = models.JSONField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

from django.db import models
import uuid

class Pricing(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    plansOptions = models.TextChoices("Plans", "Basic Standard Managed")
    plans  = models.CharField(max_length=20, choices=plansOptions, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    
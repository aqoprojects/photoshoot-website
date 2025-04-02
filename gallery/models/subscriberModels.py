from django.db import models
import uuid 

class Subscriber(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)
from django.db import models
import uuid
from django.core.exceptions import ValidationError

def validate_review_picture_size(value):
    max_size = 5 * 1024 * 1024
    if value.size > max_size:
        raise ValidationError("Image file too large (max 5 MB).")

class Review(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    name =  models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    info = models.TextField(max_length=300, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='customer_profiePic/', validators=[validate_review_picture_size],null=True, blank=True) 
    date = models.DateTimeField(auto_now_add=True)
from django.db import models
import uuid
from .categoryModels import Category
from django.core.exceptions import ValidationError

def validate_image_size(value):
    max_size = 5 * 1024 * 1024
    if value.size > max_size:
        raise ValidationError("Image file too large (max 5 MB).")


class Photo(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    picture = models.ImageField(upload_to='gallery/', max_length=1000, validators=[validate_image_size])
    date = models.DateTimeField(auto_now_add=True)

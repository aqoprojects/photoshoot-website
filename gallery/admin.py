from django.contrib import admin
from .models import Photo, Category, Service, Review, Pricing

admin.site.register(Category)
admin.site.register(Photo)
admin.site.register(Service)
admin.site.register(Review)
admin.site.register(Pricing)

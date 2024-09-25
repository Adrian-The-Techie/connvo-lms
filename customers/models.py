from django.db import models

from courses.models import Lesson

# Create your models here.


class Customer(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(null=True)
    url = models.UUIDField(null=True)
    visibility = models.BooleanField(default=True)
    courses = models.ManyToManyField(Lesson, related_name="customers")
    
    class Meta:
        ordering = ["full_name"]

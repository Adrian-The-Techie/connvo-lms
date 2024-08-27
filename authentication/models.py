from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    full_names = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(null=True)
    password = models.CharField(max_length=255)
    url = models.UUIDField(null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name

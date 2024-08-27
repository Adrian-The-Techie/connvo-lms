from cloudinary.models import CloudinaryField
from django.db import models

# Create your models here.


class Courses(models.Model):
    name = models.CharField(max_length=255, null=False)
    thumbnail = CloudinaryField("image")
    short_desc=models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(null=True,blank=True)
    url = models.UUIDField(null=True, blank=True)
    visibility = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Program"

class Chapter(models.Model):
    program=models.ForeignKey(Courses, null= True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=255, null=False)
    thumbnail = CloudinaryField("image")
    description = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(null=True,blank=True)
    url = models.UUIDField(null=True, blank=True)
    visibility = models.BooleanField(default=True)

class Lesson(models.Model):
    # program=models.ForeignKey(Chapter, null= True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=255, null=False)
    thumbnail = models.ImageField(upload_to="thumbnails/")
    video = models.FileField(upload_to="lessons/")
    description = models.CharField(max_length=255)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(null=True,blank=True)
    url = models.UUIDField(null=True, blank=True)
    visibility = models.BooleanField(default=True)

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=128)
    created_by = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)


class Filter(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)


POSTED_OBJECT_TYPE = (
    ("image", "image"),
    ("video", "video")
)

class PostedObj(models.Model):
    user = models.ForeignKey(User)
    file = models.FileField(upload_to='posted_objects/')
    type = models.CharField(max_length=128, choices=POSTED_OBJECT_TYPE)

    description = models.TextField()
    tags = models.ManyToManyField(Tag, blank=True, null=True, default=None)
    location_coordintates = models.CharField(max_length=128)
    location_name = models.CharField(max_length=128)
    image_filter = models.ForeignKey(Filter, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    likes_nmb = models.IntegerField(default=0)
    comments_nmb = models.IntegerField(default=0)


class Comment(models.Model):
    posted_object = models.ForeignKey(PostedObj)
    text = models.TextField()
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)


class Like(models.Model):
    posted_object = models.ForeignKey(PostedObj)
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)


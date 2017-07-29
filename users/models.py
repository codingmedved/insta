from django.db import models
from django.contrib.auth.models import User
from geo_locations.models import City

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User)
    city = models.ForeignKey(City)
    date_birth = models.DateField()
    age = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/')


class UserFollows(models.Model):
    user_initial = models.ForeignKey(User, related_name="user_follows_user_initial")
    user_follow = models.ForeignKey(User, related_name="user_follows_user_follow")
    is_blocked = models.BooleanField(default=False)


class UserFollowRequest(models.Model):
    user_initial = models.ForeignKey(User, related_name="user_follow_request_user_initial")
    user_follow = models.ForeignKey(User, related_name="user_follow_request_user_follow")
    is_approved = models.BooleanField(default=False)

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class DirectChat(models.Model):
    user_one = models.ForeignKey(User, related_name="user_one")
    user_two = models.ForeignKey(User, related_name="user_two")


class DirectChatMessage(models.Model):
    direct_chat = models.ForeignKey(DirectChat)
    text = models.TextField()
    user = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

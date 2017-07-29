from django.db import models


class City(models.Model):
    name = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
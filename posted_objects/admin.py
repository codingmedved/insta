from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Tag)
admin.site.register(Filter)
admin.site.register(PostedObj)
admin.site.register(Comment)
admin.site.register(Like)


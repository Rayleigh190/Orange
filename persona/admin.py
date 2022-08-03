from django.contrib import admin
from .models import Tag, Likes, Strength
# Register your models here.

admin.site.register(Tag)
admin.site.register(Likes)
admin.site.register(Strength)
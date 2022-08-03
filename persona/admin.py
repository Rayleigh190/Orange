from django.contrib import admin
from .models import Tag, Likes, Strength, Weakness, Value
# Register your models here.

admin.site.register(Tag)
admin.site.register(Likes)
admin.site.register(Strength)
admin.site.register(Weakness)
admin.site.register(Value)
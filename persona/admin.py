from django.contrib import admin
from .models import Tag, Likes, Strength, Weakness, Value, Solve, Career, Literacy
# Register your models here.

## 내부
admin.site.register(Tag)
admin.site.register(Likes)
admin.site.register(Strength)
admin.site.register(Weakness)
admin.site.register(Value)
## 외부
admin.site.register(Solve)
admin.site.register(Career)
admin.site.register(Literacy)
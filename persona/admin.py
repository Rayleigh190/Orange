from django.contrib import admin
from .models import Tag, Recommendation, Likes, Strength, Weakness, Value, Solve, Career, Literacy, Language, MBTI, HidePersona
# Register your models here.

class ModelAdmin(admin.ModelAdmin):
     readonly_fields = ('id',)


admin.site.register(Tag, ModelAdmin)
admin.site.register(Recommendation, ModelAdmin)
admin.site.register(HidePersona, ModelAdmin)

## 내부
admin.site.register(Likes, ModelAdmin)
admin.site.register(Strength, ModelAdmin)
admin.site.register(Weakness, ModelAdmin)
admin.site.register(Value, ModelAdmin)
## 외부
admin.site.register(Solve, ModelAdmin)
admin.site.register(Career, ModelAdmin)
admin.site.register(Literacy, ModelAdmin)
admin.site.register(Language, ModelAdmin)
admin.site.register(MBTI, ModelAdmin)
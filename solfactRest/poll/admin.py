from django.contrib import admin
from .models import Question


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,
         {'fields': ['title', 'is_active']}
         ),
        ('Информация о дате',
         {'fields': ['date_published'],
          'classes': ['collapse']}
         ),
    ]


admin.site.register(Question, QuestionAdmin)

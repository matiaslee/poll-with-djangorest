from django.contrib import admin

# Register your models here.

from .models import Question, Choice

admin.site.register(Question)

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('choice_text', 'question')

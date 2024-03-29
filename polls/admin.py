from django.contrib import admin

# Register your models here.
from polls.models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    fields = ["question_text"]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]

admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)
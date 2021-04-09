from django.contrib import admin

from .models import Question, Choice


class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # To reoder fields on the edit form
    fields = ['question_text', 'pub_date']
    fieldsets = [
        (None,                  {'fields': ['question_text']}),
        ('Date information',    {'fields' : ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
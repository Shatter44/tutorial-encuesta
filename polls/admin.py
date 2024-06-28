from django.contrib import admin
from .models import Choice, Question

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    inLines = [ChoiceInLine]
    list_filter = ["pub_date"]
    # fields = [(None, {"fields": ["question_text"]}),
    #     ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),]
    list_display = ["question_text", "pub_date"]
    search_fields = "question_text", "pub_date"
    
admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)


# class Question(admin.ModelAdmin):
#     @admin.display(
#         boolean=True,
#         ordering="pub_date",
#         description="Published recently?",
#     )
#     def was_published_recently(self):
#         now = timezone.now()
#         return now - datetime.timedelta(days=1) <= self.pub_date <= now
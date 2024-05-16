from django.contrib import admin

from .models import Question, Choise

#admin.site.register(Question)
#admin.site.register(Choise)

class ChoiseInline(admin.TabularInline):
    model = Choise

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines= [ChoiseInline]
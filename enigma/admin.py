from django.contrib import admin
from .models import Results, Answers
# Register your models here.
from django.contrib.sessions.models import Session


class ResultsAdmin(admin.ModelAdmin):
    list_display = ('time', 'score', 'firstname', 'lastname', 'mail', 't_answer1_1', 'tentative1_1', 't_answer1_2', 'tentative1_2', 't_answer1_3',
                    't_answer2_1', 'tentative2_1', 't_answer2_2', 'tentative2_2', 't_answer2_3', 'tentative2_3', 't_answer3_1', 'tentative3_1', 't_answer3_2', 'tentative3_2', 't_answer3_3', 'tentative3_3')
    list_filter = ('time', 'score', 'firstname', 'lastname', 'mail')


class AnswersAdmin(admin.ModelAdmin):
    list_display = ('answer1_1', 'answer1_2', 'answer1_3', 'answer2_1', 'answer2_2', 'answer2_3', 'answer3_1',
                    'answer3_2', 'answer3_3',)


admin.site.register(Results, ResultsAdmin)
admin.site.register(Answers, AnswersAdmin)
admin.site.register(Session)
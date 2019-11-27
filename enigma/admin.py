from django.contrib import admin
from .models import Results
# Register your models here.
from django.contrib.sessions.models import Session


class ResultsAdmin(admin.ModelAdmin):
    list_display = ('time', 'score', 'firstname', 'lastname', 'mail', 't_answer1_1', 'tentative1_1', 'score1_1', 't_answer1_2', 'tentative1_2', 'score1_2', 't_answer1_3', 'tentative1_3', 'score1_3',
                    't_answer2_1', 'tentative2_1', 'score2_1', 't_answer2_2', 'tentative2_2', 'score2_2', 't_answer2_3', 'tentative2_3', 'score2_3', 't_answer3_1', 'tentative3_1', 'score3_1', 't_answer3_2', 'tentative3_2', 'score3_2', 't_answer3_3', 'tentative3_3', 'score3_3')
    list_filter = ('time', 'score', 'firstname', 'lastname', 'mail')


admin.site.register(Results, ResultsAdmin)
admin.site.register(Session)
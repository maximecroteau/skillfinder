from django.db import models

# Create your models here.


class Results(models.Model):
    time = models.IntegerField()
    score = models.IntegerField()
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    mail = models.EmailField()

    t_answer1_1 = models.IntegerField()
    tentative1_1 = models.IntegerField(default=0)
    score1_1 = models.FloatField(default=0)

    t_answer1_2 = models.IntegerField()
    tentative1_2 = models.IntegerField(default=0)
    score1_2 = models.FloatField(default=0)

    t_answer1_3 = models.IntegerField()
    tentative1_3 = models.IntegerField(default=0)
    score1_3 = models.FloatField(default=0)

    t_answer2_1 = models.IntegerField()
    tentative2_1 = models.IntegerField(default=0)
    score2_1 = models.FloatField(default=0)

    t_answer2_2 = models.IntegerField()
    tentative2_2 = models.IntegerField(default=0)
    score2_2 = models.FloatField(default=0)

    t_answer2_3 = models.IntegerField()
    tentative2_3 = models.IntegerField(default=0)
    score2_3 = models.FloatField(default=0)

    t_answer3_1 = models.IntegerField()
    tentative3_1 = models.IntegerField(default=0)
    score3_1 = models.FloatField(default=0)

    t_answer3_2 = models.IntegerField()
    tentative3_2 = models.IntegerField(default=0)
    score3_2 = models.FloatField(default=0)

    t_answer3_3 = models.IntegerField()
    tentative3_3 = models.IntegerField(default=0)
    score3_3 = models.FloatField(default=0)

    class Meta:
        verbose_name = "Resultat"

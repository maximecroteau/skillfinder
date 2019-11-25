from django.db import models

# Create your models here.


class Results(models.Model):
    time = models.IntegerField()
    score = models.IntegerField()
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    mail = models.EmailField()
    t_answer1_1 = models.IntegerField()
    t_answer1_2 = models.IntegerField()
    t_answer1_3 = models.IntegerField()
    t_answer2_1 = models.IntegerField()
    t_answer2_2 = models.IntegerField()
    t_answer2_3 = models.IntegerField()
    t_answer3_1 = models.IntegerField()
    t_answer3_2 = models.IntegerField()
    t_answer3_3 = models.IntegerField()

    class Meta:
        verbose_name = "Resultat"


class Answers(models.Model):
    answer1_1 = models.CharField(max_length=50, default="Reponse")
    answer1_2 = models.CharField(max_length=50, default="Reponse")
    answer1_3 = models.CharField(max_length=50, default="Reponse")
    answer2_1 = models.CharField(max_length=50, default="Reponse")
    answer2_2 = models.CharField(max_length=50, default="Reponse")
    answer2_3 = models.CharField(max_length=50, default="Reponse")
    answer3_1 = models.CharField(max_length=50, default="Reponse")
    answer3_2 = models.CharField(max_length=50, default="Reponse")
    answer3_3 = models.CharField(max_length=50, default="Reponse")

    class Meta:
        verbose_name = "Reponse"

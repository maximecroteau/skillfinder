from django.db import models

# Create your models here.


class Results(models.Model):
    Time = models.IntegerField()
    Score = models.IntegerField()
    Firstname = models.CharField(max_length=30)
    Lastname = models.CharField(max_length=30)
    Mail = models.EmailField()
    T_Answer1_1 = models.IntegerField()
    T_Answer1_2 = models.IntegerField()
    T_Answer1_3 = models.IntegerField()
    T_Answer2_1 = models.IntegerField()
    T_Answer2_2 = models.IntegerField()
    T_Answer2_3 = models.IntegerField()
    T_Answer3_1 = models.IntegerField()
    T_Answer3_2 = models.IntegerField()
    T_Answer3_3 = models.IntegerField()

    class Meta:
        verbose_name = "Resultats"


class Answers(models.Model):
    Answer1_1 = models.CharField(max_length=50, default="Reponse")
    Answer1_2 = models.CharField(max_length=50, default="Reponse")
    Answer1_3 = models.CharField(max_length=50, default="Reponse")
    Answer2_1 = models.CharField(max_length=50, default="Reponse")
    Answer2_2 = models.CharField(max_length=50, default="Reponse")
    Answer2_3 = models.CharField(max_length=50, default="Reponse")
    Answer3_1 = models.CharField(max_length=50, default="Reponse")
    Answer3_2 = models.CharField(max_length=50, default="Reponse")
    Answer3_3 = models.CharField(max_length=50, default="Reponse")

    class Meta:
        verbose_name = "Reponses"

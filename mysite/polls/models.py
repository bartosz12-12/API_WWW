from django.db import models

class Person(models.Model):
    class Plec(models.IntegerChoices):
        MEN = 1
        WOMEN = 2
        DIFFRENT = 3
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    sex = models.IntegerField(choices=Plec.choices)
    date_of_birth = models.DateField()

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
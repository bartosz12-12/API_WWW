from django.db import models
from django.core.exceptions import ValidationError

def validate_rating(value):
    if value < 1 or value > 10:
        raise ValidationError("Ocena mięsa musi być w skali od 1 do 10.")

class Person(models.Model):
    class Plec(models.IntegerChoices):
        MEN = 1
        WOMEN = 2
        DIFFRENT = 3
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    sex = models.IntegerField(choices=Plec.choices)
    date_of_birth = models.DateField()

class Restaurant(models.Model):
    class Type(models.IntegerChoices):
        KEBAB = 1
        ZAPIEKANKA = 2
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    typeRestaurant = models.IntegerField(choices=Type.choices)

class RatingKebaba(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    meat =  models.IntegerField(default=0, help_text="Ocena miesa w skali od 1 do 10",validators = [validate_rating])
    sauce = models.IntegerField(default=0, help_text="Ocena sosu w skali od 1 do 10",validators = [validate_rating])
    vegetables = models.IntegerField(default=0, help_text="Ocena warzyw w skali od 1 do 10",validators = [validate_rating])
    additions = models.IntegerField(default=0, help_text="Ocena dodatkow w skali od 1 do 10",validators = [validate_rating])
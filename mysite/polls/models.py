from django.core.validators import validate_integer
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
    wlasciciel=models.ForeignKey('auth.User', on_delete=models.CASCADE)

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
    meat = models.IntegerField(default=0, help_text="Ocena miesa w skali od 1 do 10",validators = [validate_rating])
    sauce = models.IntegerField(default=0, help_text="Ocena sosu w skali od 1 do 10",validators = [validate_rating])
    vegetables = models.IntegerField(default=0, help_text="Ocena warzyw w skali od 1 do 10",validators = [validate_rating])
    additions = models.IntegerField(default=0, help_text="Ocena dodatkow w skali od 1 do 10",validators = [validate_rating])
    final_grade = models.FloatField(default=0.0, help_text="Ostateczna ocena", validators=[validate_integer],editable=False)

    def calculate_final_grade(self):
        # Oblicz średnią z oceny mięsa, sosu, warzyw i dodatków
        ratings = [self.meat, self.sauce, self.vegetables, self.additions]
        non_zero_ratings = [rating for rating in ratings if rating > 0]

        if non_zero_ratings:
            average_rating = sum(non_zero_ratings) / len(non_zero_ratings)
            self.final_grade = round(average_rating, 2)
        else:
            # Jeżeli brak ocen, ustaw final_grade na 0
            self.final_grade = 0.0

    def save(self, *args, **kwargs):
        # Przed zapisaniem obiektu, oblicz final_grade
        self.calculate_final_grade()
        super().save(*args, **kwargs)

class RatingZapiekanka(models.Model):
    person = models.ForeignKey(Person,on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)
    bread = models.IntegerField(default=0, help_text="Ocena pieczywa w skali od 1 do 10",validators = [validate_rating])
    cheese = models.IntegerField(default=0, help_text="Ocena sera w skali od 1 do 10",validators = [validate_rating])
    sauce = models.IntegerField(default=0, help_text="Ocena sosu w skali od 1 do 10",validators = [validate_rating])
    additions = models.IntegerField(default=0, help_text="Ocena dodatkow w skali od 1 do 10",validators = [validate_rating])
    final_grade = models.FloatField(default=0.0, help_text="Ostateczna ocena", validators=[validate_integer],
                                    editable=False)

    def calculate_final_grade(self):
        ratings = [self.bread, self.cheese, self.sauce, self.additions]
        non_zero_ratings = [rating for rating in ratings if rating > 0]

        if non_zero_ratings:
            average_rating = sum(non_zero_ratings) / len(non_zero_ratings)
            self.final_grade = round(average_rating, 2)
        else:
            self.final_grade = 0.0

    def save(self, *args, **kwargs):
        self.calculate_final_grade()
        super().save(*args, **kwargs)
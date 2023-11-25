from django.contrib import admin

from .models import *

class TabPerson(admin.ModelAdmin):
    list_display = ['id', 'name','surname','sex','date_of_birth']

class TabRKebab(admin.ModelAdmin):
    list_display = ['id', 'person_display','restaurant_display','meat','sauce','vegetables','additions','final_grade']

    @admin.display(description='person')
    def person_display(self, obj):
        return f'{obj.person.name} {obj.person.surname}'

    @admin.display(description='restaurant')
    def restaurant_display(self, obj):
        return f'{obj.restaurant.name}'

class TabRestaurant(admin.ModelAdmin):
    list_display = ['id', 'name','country','city','street','typeRestaurant']
admin.site.register(Person,TabPerson)
admin.site.register(Restaurant,TabRestaurant)
admin.site.register(RatingKebaba,TabRKebab)

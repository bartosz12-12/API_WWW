from rest_framework import serializers
from .models import *

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id','name','surname','sex','date_of_birth']
        read_only_fields=['id']

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id','name','country','city','street','typeRestaurant']
        read_only_fields=['id']

    def create(self, validated_data):
        return Restaurant.objects.create(**validated_data)

class RatingKebabaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingKebaba
        fields = ['id','person','restaurant','meat','sauce','vegetables','additions','final_grade']
        read_only_fields=['id']

    def create(self, validated_data):
        return RatingKebaba.objects.create(**validated_data)

class RatingZapiekankaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RatingZapiekanka
        fields = ['id','person','restaurant','bread','cheese','sauce','additions','final_grade']
        read_only_fields=['id']

    def create(self, validated_data):
        return RatingZapiekanka.objects.create(**validated_data)
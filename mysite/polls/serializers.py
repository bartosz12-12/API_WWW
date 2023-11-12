from rest_framework import serializers
from .models import *

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id','name','surname','sex','date_of_birth']
        read_only_fields=['id']

    def create(self, validated_data):
        return Person.objects.create(**validated_data)

class RestaurantSerializer(serializers.Serializer):
    class Meta:
        model = Restaurant
        fields = ['id','name','country','city','street','typeRestaurant']
        read_only_fields=['id']

    def create(self, validated_data):
        return Restaurant.objects.create(**validated_data)

class RatingKebabaSerializer(serializers.Serializer):
    class Meta:
        model = RatingKebaba
        fields = ['id','person','restaurant','meat','sauce','vegetables','additions']
        read_only_fields=['id']

    def create(self, validated_data):
        return RatingKebaba.objects.create(**validated_data)
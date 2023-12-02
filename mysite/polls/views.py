from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import Http404, HttpResponseForbidden
from .models import Person, Restaurant, RatingKebaba, RatingZapiekanka
from .serializers import PersonSerializer, RestaurantSerializer, RatingKebabaSerializer, RatingZapiekankaSerializer

@api_view(['GET','POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def person_list(request):
    if request.method == 'GET':
        persons = Person.objects.all()
        serializer = PersonSerializer(persons, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def person_detail(request, pk):
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        person = Person.objects.get(pk=pk)
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','Delete'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
@permission_required('polls.delete_person', raise_exception=True)
def person_delete(request,pk):
    try:
        person = Person.objects.get(pk=pk)
        if request.method == 'GET':
            person = Person.objects.get(pk=pk)
            serializer = PersonSerializer(person)
            return Response(serializer.data)
        if request.method == 'DELETE':
            person.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET','POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def restaurant_list(request):
    if request.method == 'GET':
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def restaurant_detail(request, pk):
    try:
        restaurant = Restaurant.objects.get(pk=pk)
    except Restaurant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        restaurant = Restaurant.objects.get(pk=pk)
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RestaurantSerializer(restaurant, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        restaurant.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','Delete'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
@permission_required('polls.delete_restaurant', raise_exception=True)
def restaurant_delete(request,pk):
    try:
        restaurant = Restaurant.objects.get(pk=pk)
        if request.method == 'GET':
            restaurant = Restaurant.objects.get(pk=pk)
            serializer = RestaurantSerializer(restaurant)
            return Response(serializer.data)
        if request.method == 'DELETE':
            restaurant.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET','POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def rating_kebab_list(request):
    if request.method == 'GET':
        kebab = RatingKebaba.objects.all()
        serializer = RatingKebabaSerializer(kebab, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = RatingKebabaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def rating_kebab_detail(request, pk):
    try:
        kebab = RatingKebaba.objects.get(pk=pk)
    except RatingKebaba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        kebab = RatingKebaba.objects.get(pk=pk)
        serializer = RatingKebabaSerializer(kebab)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RatingKebabaSerializer(kebab, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        kebab.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def rating_zapiekanka_list(request):
    if request.method == 'GET':
        zapiekanka = RatingZapiekanka.objects.all()
        serializer = RatingZapiekankaSerializer(zapiekanka, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = RatingZapiekankaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def rating_zapiekanka_detail(request, pk):
    try:
        zapiekanka = RatingZapiekanka.objects.get(pk=pk)
    except RatingZapiekanka.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        zapiekanka = RatingZapiekanka.objects.get(pk=pk)
        serializer = RatingZapiekankaSerializer(zapiekanka)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RatingZapiekankaSerializer(zapiekanka, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        zapiekanka.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def restaurant_rating_kebab(request,pk):
    if request.method == 'GET':
        ratings = RatingKebaba.objects.filter(restaurant_id=pk)
        serializer = RatingKebabaSerializer(ratings, many=True)
        return Response(serializer.data)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def restaurant_rating_zapiekanka(request,pk):
    if request.method == 'GET':
        ratings = RatingZapiekanka.objects.filter(restaurant_id=pk)
        serializer = RatingZapiekankaSerializer(ratings, many=True)
        return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def rating_zapiekanka_person(request,pk):
    if request.method == 'GET':
        ratings = RatingZapiekanka.objects.filter(person=pk)
        serializer = RatingZapiekankaSerializer(ratings, many=True)
        return Response(serializer.data)



@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def rating_kebab_person(request,pk):
    if request.method == 'GET':
        ratings = RatingKebaba.objects.filter(person=pk)
        serializer = RatingKebabaSerializer(ratings, many=True)
        return Response(serializer.data)


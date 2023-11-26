from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from . import views

urlpatterns = [
    path('persons/', views.PersonList.as_view()),
    path('person/<int:pk>/', views.PersonDetail.as_view()),
    path('restaurants/', views.RestaurantList.as_view()),
    path('restaurant/<int:pk>/', views.RestaurantDetail.as_view()),
    path('rating/kebab', views.RatingKebabaList.as_view()),
    path('rating/kebab/<int:pk>/', views.RatingKebabaList.as_view()),
    path('rating/zapiekanka', views.RatingZapiekankiList.as_view()),
    path('rating/zapiekanka/<int:pk>/', views.RatingZapiekankiDetail.as_view()),
    path('restaurant/kebab/<int:pk>/', views.RestaurantRatingKebab.as_view()),
    path('restaurant/zapiekanka/<int:pk>/', views.RestaurantRatingZapiekanka.as_view()),

]
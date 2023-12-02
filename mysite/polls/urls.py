from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from . import views

urlpatterns = [
    path('persons/', views.person_list),
    path('person/<int:pk>/', views.person_detail),
    path('person/delete/<int:pk>/', views.person_delete),
    path('restaurants/', views.restaurant_list),
    path('restaurant/<int:pk>/', views.restaurant_detail),
    path('restaurant/delete/<int:pk>/', views.restaurant_delete),
    path('rating/kebab', views.rating_kebab_list),
    path('rating/kebab/<int:pk>/', views.rating_kebab_detail),
    path('rating/zapiekanka', views.rating_zapiekanka_list),
    path('rating/zapiekanka/<int:pk>/', views.rating_zapiekanka_detail),
    path('restaurant/kebab/<int:pk>/', views.restaurant_rating_kebab),
    path('restaurant/zapiekanka/<int:pk>/', views.restaurant_rating_zapiekanka),
    path('rating/zapiekanka/person/<int:pk>/', views.rating_zapiekanka_person),
    path('rating/kebab/person/<int:pk>/', views.rating_kebab_person),
]
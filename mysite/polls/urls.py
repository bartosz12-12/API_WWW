from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path, include
from . import views

urlpatterns = [
    path('persons/', views.PersonList.as_view()),
    path('persons/<int:pk>/', views.PersonDetail.as_view()),
]
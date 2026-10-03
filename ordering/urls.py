from django.urls import path
from . import views

urlpatterns = [
    path('', views.ordering, name='ordering'),
    path('treats/', views.treats, name='treats'),
    path('breakfast/', views.breakfast, name='breakfast'),
    path('coffee/', views.coffee, name='coffee'),
    path('familymeals/', views.family_meals, name='family_meals'),
    path('kidsmeals/', views.kids_meals, name='kids_meals'),
    path('meals/', views.meals, name='meals'),
    path('salads/', views.salads, name='salads'),
    path('sauces/', views.sauces, name='sauces'),
]
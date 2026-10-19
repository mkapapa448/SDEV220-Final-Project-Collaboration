from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('treats/', views.treats, name='treats'),
    path('breakfast/', views.breakfast, name='breakfast'),
    path('familymeals/', views.family_meals, name='family_meals'),
    path('kidsmeals/', views.kids_meals, name='kids_meals'),
    path('meals/', views.meals, name='meals'),
    path('salads/', views.salads, name='salads'),
    path('sauces/', views.sauces, name='sauces'),
    path('drinks/', views.drinks, name='drinks'),
    path('sides/', views.sides, name='sides'),
    path('entrees/', views.entrees, name='entrees'),
    path('addorder/', views.add_order, name='add_order'),
    path('cart/', views.view_cart, name='view_cart'),
    path('placedorder/', views.place_order, name='place_order'),
    path('removeitem/', views.remove_item, name='remove_item'),
]
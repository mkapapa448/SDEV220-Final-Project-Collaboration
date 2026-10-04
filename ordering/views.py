from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def drinks(request):
    soda_menu = {
        "Chicken-Cola": 2.45,
        "Diet Chicken": 2.45,
        "Chicken-Cola Cherry": 2.45,
        "Sprite": 2.45,
        "Dr Pepper": 2.45,
        "Diet Dr Pepper": 2.45,
        "Mello Yello": 2.45,
    }

    lemonade_teas_menu = {
        "Pineapple Dragonfruit Lemonade": 3.59,
        "Pineapple Dragonfruit Sunjoy": 3.59,
        "Pineapple Dragonfruit Teas": 3.15,
        "Freshly-Brewed Sweetened Iced Tea": 2.45,
        "Freshly-Brewed Unsweetened Iced Tea": 2.45,
        "Kickin Lemonade": 2.79,
        "Kickin Diet Lemonade": 2.79,
    }

    coffee_menu = {
        "Iced Coffee": 4.19,
        "Cream Cold Brew": 4.79,
        "Hot Coffee": 2.29,
    }

    milk_menu = {
        "Milk": 1.99,
        "Chocolate Milk": 1.99,
        "Strawberry Milk": 1.99,
    }

    juices_water_menu = {
        "Hi-C Fruit Punch": 2.45,
        "Bottled Water": 2.39,
        "Apple Juice": 1.99,
    }

    return render(request, 'ordering/drinks.html', {
        "soda": soda_menu,
        "coffee": coffee_menu,
        "milk": milk_menu,
        "lemonade_tea": lemonade_teas_menu,
        "juices_water": juices_water_menu,
    })

def treats(request):
    treats_menu = {
        "Strawberry Milkshake": 4.95,
        "Chocolate Milkshake": 4.95,
        "Vanilla Milkshake": 4.95,
        "Cookies & Cream Milkshade": 4.95,
        "Frosted Kickenade": 4.75,
        "Chocolate Brownie": 2.29,
        "Chocolate Cookie": 1.79,
        "Ice Cream Cone": 1.89,
        "Ice Cream Cup": 1.69,
    }

    return render(request, 'ordering/treats.html', {'treats': treats_menu})

def breakfast(request):
    original_breakfast_menu = {
        "Chicken & Waffles Breakfast Sandwich W/ Chicken & Waffles Sandwich Filet Meal": 8.79,
        "Kickin Chicken Biscuit Meal": 7.25,
        "Mini Chicken Meal": 8.35,
        "Kicken Minis": 8.35,
        "Chicken & Waffles Breakfast Sandwich w/ Filet Meal": 5.49,
        "Hash Browns": 1.75,
        "Breakfast Waffle": 1.65,
        "Breakfast Biscuit": 1.65,
    }

    spicy_breakfast_menu = {
        "Chicken and Waffles Breakfast Sandwich W/ Spicy Filet Meal": 9.05,
        "Kickin Chicken Spicy Chicken Biscuit Meal": 7.49,
        "Chicken & Waffles breakfast Sandwich w/ Spicy Filet Meal": 5.75,
    }

    fruits_menu = {
        "Berry Parfait": 4.99,
        "Fruit Cup": 4.29,
    }

    return render(request, 'ordering/breakfast.html', {
        'original_breakfast': original_breakfast_menu,
        'spicy_breakfast': spicy_breakfast_menu,
        'fruits': fruits_menu,

        })

def family_meals(request):
    family_menu = {
        "Kickin Chicken Nuggets Family Style": 32.49,
        "Kickin Chicken Kickn' Strips Family Meal": 32.49,
        "Grilled Nugget Family Style": 35.49
    }

    return render(request, 'ordering/family_meals.html', {'family_meals': family_menu})

def kids_meals(request):
    kids_meal_menu = {
        "5 CT Kickin Nuggets Meal": 3.40,
        "2 Ct Kickin Strips Meal": 6.95,
        "5 Ct Grilled Kickin Nuggets Meal": 7.05,
        "Mac and Cheese Kid's Meal": 7.05
    }
    return render(request, 'ordering/kids_meals.html', {'kids_meals': kids_meal_menu})

def meals(request):
    chicken_waffles_menu = {
        "Chicken & Waffles Sandwich Filet Meal": 12.49,
        "Chicken & Waffles Sandwich Spicy Filet Meal": 12.89,
        "Chicken & Waffles Sandwich Grilled Filet Meal": 13.25,
    }

    spicy_chicken_menu = {
        "Kicken Chicken Spicy Sandwich Meal": 9.85,
        "Spicy Chicken Deluxe Meal": 10.65,
    }

    original_chicken_menu = {
        "Grilled Chicken Sandwich": 10.99,
        "Grilled Chicken Club Meal": 12.89,
        "Kicken Chicken Sandwich Meal": 9.45,
        "Kicken Chicken Deluxe Meal": 10.25
    }

    chicken_strip_menu = {
        "Kickin Chicken Nuggets Meal": 9.55,
        "Kicken Chicken Grilled Nuggets Meal": 10.39,
        "Chicken Strips Meal": 9.89
    }

    return render(request, 'ordering/meals.html', {
        'chicken_waffles': chicken_waffles_menu,
        'spicy_chicken': spicy_chicken_menu,
        'original_chicken': original_chicken_menu,
        'chicken_strips': chicken_strip_menu
    })

def salads(request):
    salad_menu = {
        "Cobb Salad": 9.89,
        "Market Salad": 10.09,
        "Kickin' Salad": 11.25
    }

    return render(request, 'ordering/salads.html', {'salads': salad_menu})

def sauces(request):
    sauces_menu = {
        "8oz Kickin Chicken Sauce (Spicy)": 3.00,
        "8oz Honey Mustard Sauce": 3.00,
        "8oz Barbecue Sauce": 2.75,
        "8oz Kickin Sauce (Regular)": 3.00,
        "8oz Saucy Chicken Ranch": 2.75
    }

    return render(request, 'ordering/sauces.html', {'sauces': sauces_menu})

from django.shortcuts import render, redirect
from django.http import HttpResponse


#All functions return the proper menus. Due to the scope I brought all of the menu's outside
#This helps track the cost of every item globally instead of locally.

def ordering(request):
    return render(request, 'ordering/ordering.html')

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

def drinks(request):
    return render(request, 'ordering/drinks.html', {
        "soda": soda_menu,
        "coffee": coffee_menu,
        "milk": milk_menu,
        "lemonade_tea": lemonade_teas_menu,
        "juices_water": juices_water_menu,
    })

treats_menu = {
    "Strawberry Milkshake": 4.95,
    "Chocolate Milkshake": 4.95,
    "Vanilla Milkshake": 4.95,
    "Cookies & Cream Milkshade": 4.95,
    "Frosted Kickinade": 4.75,
    "Chocolate Brownie": 2.29,
    "Chocolate Cookie": 1.79,
    "Ice Cream Cone": 1.89,
    "Ice Cream Cup": 1.69,
}

def treats(request):
    return render(request, 'ordering/treats.html', {'treats': treats_menu})

original_breakfast_menu = {
    "Chicken & Waffles Breakfast Sandwich w/ Kickin Filet": 8.79,
    "Kickin Chicken Biscuit Meal": 7.25,
    "Mini Chicken Meal": 8.35,
    "Kickin Minis": 8.35,
    "Chicken & Waffles Breakfast Sandwich w/ Filet Meal": 5.49,
    "Hash Browns": 1.75,
    "Breakfast Waffle": 1.65,
    "Breakfast Biscuit": 1.65,
}

spicy_breakfast_menu = {
    "Chicken and Waffles Breakfast Sandwich w/ Spicy Filet Meal": 9.05,    
    "Kickin Chicken Spicy Chicken Biscuit Meal": 7.49,
    "Chicken & Waffles breakfast Sandwich w/ Spicy Filet Meal": 5.75,
}

fruits_menu = {
    "Berry Parfait": 4.99,
    "Fruit Cup": 4.29,
}

def breakfast(request):
    return render(request, 'ordering/breakfast.html', {
        'original_breakfast': original_breakfast_menu,
        'spicy_breakfast': spicy_breakfast_menu,
        'fruits': fruits_menu,

        })

family_menu = {
    "Kickin Chicken Nuggets Family Style": 32.49,
    "Kickin Chicken Kickn' Strips Family Meal": 32.49,
    "Grilled Nugget Family Style": 35.49,
}

def family_meals(request):
    return render(request, 'ordering/family_meals.html', {'family_meals': family_menu})

kids_meal_menu = {
    "5 CT Kickin Nuggets Meal": 3.40,
    "2 Ct Kickin Strips Meal": 6.95,
    "5 Ct Grilled Kickin Nuggets Meal": 7.05,
    "Mac and Cheese Kid's Meal": 7.05,
}
def kids_meals(request):
    return render(request, 'ordering/kids_meals.html', {'kids_meals': kids_meal_menu})

chicken_waffles_menu = {
    "Chicken & Waffles Sandwich Filet Meal": 12.49,
    "Chicken & Waffles Sandwich Spicy Filet Meal": 12.89,
    "Chicken & Waffles Sandwich Grilled Filet Meal": 13.25,
}

spicy_chicken_menu = {
    "Kickin Chicken Spicy Sandwich Meal": 9.85,
    "Spicy Chicken Deluxe Meal": 10.65,
}

original_chicken_menu = {
    "Grilled Chicken Sandwich": 10.99,
    "Grilled Chicken Club Meal": 12.89,
    "Kickin Chicken Sandwich Meal": 9.45,
    "Kickin Chicken Deluxe Meal": 10.25,
}

chicken_strip_menu = {
    "Kickin Chicken Nuggets Meal": 9.55,
    "Kickin Chicken Grilled Nuggets Meal": 10.39,
    "Chicken Strips Meal": 9.89,
}

def meals(request):
    return render(request, 'ordering/meals.html', {
        'chicken_waffles': chicken_waffles_menu,
        'spicy_chicken': spicy_chicken_menu,
        'original_chicken': original_chicken_menu,
        'chicken_strips': chicken_strip_menu
    })

salad_menu = {
    "Cobb Salad": 9.89,
    "Market Salad": 10.09,
    "Kickin' Salad": 11.25,
}

def salads(request):
    return render(request, 'ordering/salads.html', {'salads': salad_menu})

sauces_menu = {
    "8oz Kickin Chicken Sauce (Spicy)": 3.00,
    "8oz Honey Mustard Sauce": 3.00,
    "8oz Barbecue Sauce": 2.75,
    "8oz Kickin Sauce (Regular)": 3.00,
    "8oz Saucy Chicken Ranch": 2.75,
}

def sauces(request):
    return render(request, 'ordering/sauces.html', {'sauces': sauces_menu})

sides_menu = {
    "Kickin Chicken Waffle Fries": 2.65,
    "Fruit Cup": 4.29,
    "Side Salad": 4.39,
    "Mac & Cheese": 4.29,
    "Kale Crunch Side": 4.29,
    "Berry Parfait": 4.99,
    "Apple Sauce": 2.49,
    "Cheese Sauce": 1.55,
}

def sides(request):
    return render(request, 'ordering/sides.html', {'sides': sides_menu})

original_entree_menu = {
    "Chicken & Waffles Sandwich w/ Kickin' Filet": 8.39,
    "Chicken & Waffles Sandwich w/ Grilled Filet": 9.15,
    "Kickin' Chicken Sandwich": 5.29,
    "Kickin' Deluxe Sandwich": 6.09,
    "Kickin' Chicken Cool Wrap": 6.85,
    "Grilled Chicken Sandwich": 6.85,
    "Kickin' Chicken Grilled Club Sandwich": 8.75,
}

spicy_entree_menu = {
    "Chicken & Waffles Sandwich w/ Spicy Kickin' Filet": 8.79,
    "Spicy Deluxe Sandwich": 6.49,
    "Spicy Kickin' Sandwich": 5.69,
}

nugget_menu = {
    "Kickin Nuggets": 5.39,
    "Grilled Kickin Nuggets": 6.19,
    "Kickin Chicken Tenders": 5.65,
}

def entrees(request):
    return render(request, 'ordering/entrees.html', {
        'original_entree': original_entree_menu,
        'spicy_entree': spicy_entree_menu,
        'nugget_entree': nugget_menu,
    })

#this list controls the menu's list globally so we can get accurate pricing.

all_menus = {
    **original_entree_menu,
    **spicy_entree_menu,
    **nugget_menu,
    **soda_menu,
    **lemonade_teas_menu,
    **coffee_menu,
    **milk_menu,
    **juices_water_menu,
    **original_breakfast_menu,
    **spicy_breakfast_menu,
    **fruits_menu,
    **family_menu,
    **kids_meal_menu,
    **chicken_waffles_menu,
    **spicy_chicken_menu,
    **original_chicken_menu,
    **chicken_strip_menu,
    **salad_menu,
    **sauces_menu,
    **sides_menu,
    **treats_menu,
}

def add_order(request):
    if request.method == 'POST':
        item = request.POST.get('item_name')
        category = request.POST.get('category')

        print(f"Selected item: {item}")

        cart = request.session.get('cart', {})
        cart[item] = cart.get(item, 0) + 1

        request.session['cart'] = cart

        allowed_categories = [
            'drinks', 'salads', 'treats',
            'sides', 'entrees', 'breakfast',
            'sauces', 'ordering', 'family_meals',
            'kids_meals', 'meals', 'cart'
        ]

        if category in allowed_categories:
            return redirect(category)

        return redirect('ordering')
    return HttpResponse("Method not allowed.", status=405)

def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0

    for item, quantity in cart.items():
        if item in all_menus:
            price = all_menus[item]
            subtotal = price * quantity
            total += subtotal

            cart_items.append({
                'name': item,
                'quantity': quantity,
                'price': price,
                'subtotal': subtotal,
            })

    tax = round(total * .07, 2)
    grand_total = total + tax

    return render(request, 'ordering/checkout.html', {
        'cart_items': cart_items,
        'total': total,
        'tax': tax,
        'grand_total': grand_total
    })

def place_order(request):
    if request.method =='POST':
        cart = request.session.get('cart', {})

        if not cart:
            return redirect('view_cart')

        request.session['cart'] = {}

        return render(request, 'ordering/place_order.html',)
    return redirect('view_cart')

def remove_item(request):
    if request.method =='POST':
        item = request.POST.get('item_name')
        cart = request.session.get('cart', {})

        if item in cart:
            cart[item] -=1
            
            if cart[item] <= 0:
                del cart[item]

            request.session['cart'] = cart
        return redirect('view_cart')

    return HttpResponse("Method not allowed.", status=405)
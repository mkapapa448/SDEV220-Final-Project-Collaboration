from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def ordering(request):
    return render(request, 'ordering/home.html')

def drinks(request):
    return render(request, 'ordering/drinks.html')

def treats(request):
    return render(request, 'ordering/treats.html')

def breakfast(request):
    return render(request, 'ordering/breakfast.html')

def coffee(request):
    return render(request, 'ordering/coffee.html')

def family_meals(request):
    return render(request, 'ordering/family_meals.html')

def kids_meals(request):
    return render(request, 'ordering/kids_meals.html')

def meals(request):
    return render(request, 'ordering/meals.html')

def salads(request):
    return render(request, 'ordering/salads.html')

def sauces(request):
    return render(request, 'ordering/sauces.html')

from django.shortcuts import render
from .models import Recipe
import random

def main(request):
    all_recipes = list(Recipe.objects.all())
    random_recipes = random.sample(all_recipes, min(len(all_recipes), 10))  # до 10
    return render(request, 'main.html', {'recipes': random_recipes})

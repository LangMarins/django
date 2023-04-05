from datetime import datetime
from django.http.response import HttpResponse
from django.shortcuts import render

all_foods = [
    {'id': 1, 'title': 'Dark Choco Premium', 'price': 349, 'is_premium': True, 'promotion_end_at': datetime(2023, 5, 31)},
    {'id': 2, 'title': 'Red Spicy', 'price': 349, 'is_premium': False, 'promotion_end_at': datetime(2023, 5, 13)},
    {'id': 3, 'title': 'Bluce Glacier', 'price': 349, 'is_premium': False, 'promotion_end_at': datetime(2023, 5, 13)},
]

# Create your views here.

def foods(request):
    context = { 'foods': all_foods}
    return render(request, 'app_foods/foods.html', context)

def food(request, food_id):
    one_food = None
    try:
        one_food = [f for f in all_foods if f['id'] == food_id][0]
        
    except IndexError:
        print('ไม่มีข้อมูล')
        
    context = { 'food': one_food }
    return render(request, 'app_foods/food.html', context)

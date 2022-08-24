from math import ceil

number_of_days = int(input())
food_left_kg = int(input())
food_for_dog_per_day = float(input())
food_for_cat_per_day = float(input())
food_for_turtle_per_day = float(input()) / 1000

total_food_per_day = food_for_dog_per_day + food_for_cat_per_day + food_for_turtle_per_day
total_food_needed = total_food_per_day * number_of_days

if food_left_kg >= total_food_needed:
    print(f'{int(food_left_kg - total_food_needed)} kilos of food left.')
else:
    print(f'{ceil(total_food_needed - food_left_kg)} more kilos of food are needed.')
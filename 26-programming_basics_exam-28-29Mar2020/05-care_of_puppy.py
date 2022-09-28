total_food = int(input()) * 1000

total_food_eaten = 0

while True:
    food_eaten = input()
    if food_eaten == "Adopted":
        break
    else:
        food_eaten = int(food_eaten)
        total_food_eaten += food_eaten

if total_food_eaten > total_food:
    needed_food = total_food_eaten - total_food
    print(f'Food is not enough. You need {needed_food} grams more.')
else:
    difference = total_food - total_food_eaten
    print(f'Food is enough! Leftovers: {difference} grams.')
days = int(input())
total_food = float(input())

food_eaten_by_dog = 0
food_eaten_by_cat = 0
total_eaten_biscuits = 0

for day in range(1, days + 1):
    today_food_eaten_by_dog = float(input())
    food_eaten_by_dog += today_food_eaten_by_dog
    today_food_eaten_by_cat = float(input())
    food_eaten_by_cat += today_food_eaten_by_cat
    if day % 3 == 0:
        biscuits = (today_food_eaten_by_dog + today_food_eaten_by_cat) * .1
        total_eaten_biscuits += biscuits

print(f"Total eaten biscuits: {int(total_eaten_biscuits)}gr.")
total_eaten_food = food_eaten_by_cat + food_eaten_by_dog
percent_eaten_food = total_eaten_food / total_food * 100
print(f"{percent_eaten_food:.2f}% of the food has been eaten.")
percent_eaten_food_byd_dog = food_eaten_by_dog / total_eaten_food * 100
print(f"{percent_eaten_food_byd_dog:.2f}% eaten from the dog.")
percent_eaten_food_byd_cat = food_eaten_by_cat / total_eaten_food * 100
print(f"{percent_eaten_food_byd_cat:.2f}% eaten from the cat.")
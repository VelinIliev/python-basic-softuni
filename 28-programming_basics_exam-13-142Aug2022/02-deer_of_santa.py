from math import ceil
days_sanata_claus_missing = int(input())
food_left_behind = int(input())
food_per_day_for_first_deer = float(input())
food_per_day_for_second_deer = float(input())
food_per_day_for_third_deer = float(input())

food_per_day_for_all_deer = food_per_day_for_first_deer + food_per_day_for_second_deer + food_per_day_for_third_deer
total_food_needed = food_per_day_for_all_deer * days_sanata_claus_missing

if total_food_needed <= food_left_behind:
    remaining_kilos = int(food_left_behind - total_food_needed)
    print(f'{remaining_kilos} kilos of food left.')
else:
    diffrence = ceil(total_food_needed - food_left_behind)
    print(f'{diffrence} more kilos of food are needed.')
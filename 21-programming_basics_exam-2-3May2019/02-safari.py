budget = float(input())
fuel_needed = float(input())
day_of_week = input()

fuel_price_per_l = 2.10
guide_price = 100

total = fuel_price_per_l * fuel_needed + guide_price

if day_of_week == "Saturday":
    total *= .9
elif day_of_week == "Sunday":
    total *= .8

if budget >= total:
    print(f'Safari time! Money left: {budget - total:.2f} lv.')
else:
    print(f'Not enough money! Money needed: {total - budget:.2f} lv.')
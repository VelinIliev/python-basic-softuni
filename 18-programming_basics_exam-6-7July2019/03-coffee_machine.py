drink_type = input()
sugar_state = input()
number_of_drinks = int(input())
total = 0

if sugar_state == "Without":
    espresso_price = .9
    cappuccino_price = 1
    tea_price = .5
elif sugar_state == "Normal":
    espresso_price = 1
    cappuccino_price = 1.2
    tea_price = .6
elif sugar_state == "Extra":
    espresso_price = 1.2
    cappuccino_price = 1.6
    tea_price = .7

if drink_type == "Espresso":
    total += espresso_price * number_of_drinks
elif drink_type == "Cappuccino":
    total += cappuccino_price * number_of_drinks
elif drink_type == "Tea":
    total += tea_price * number_of_drinks


if sugar_state == "Without":
    total *= .65
if drink_type == "Espresso" and number_of_drinks >= 5:
    total *= .75
if total > 15:
    total *= .8

print(f'You bought {number_of_drinks} cups of {drink_type} for {total:.2f} lv.')

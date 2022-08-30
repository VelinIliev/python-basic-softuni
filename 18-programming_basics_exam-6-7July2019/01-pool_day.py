from math import ceil

number_of_people = int(input())
entrance_fee = float(input())
deck_chair_price = float(input())
umbrella_price = float(input())

total_fee = number_of_people * entrance_fee

number_of_umbrellas = ceil(number_of_people / 2)
total_umbrellas = number_of_umbrellas * umbrella_price

number_of_deck_chairs = ceil(number_of_people * .75)
total_deck_chairs = number_of_deck_chairs * deck_chair_price

total = total_fee + total_umbrellas + total_deck_chairs

print(f'{total:.2f} lv.')

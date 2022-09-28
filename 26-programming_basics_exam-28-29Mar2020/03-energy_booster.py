fruit = input()
set_size = input()
set_number = int(input())

energy_gel_price_per_piece = 0
pieces = 0

if fruit == "Watermelon":
    if set_size == "small":
        energy_gel_price_per_piece = 56
        pieces = 2
    elif set_size == "big":
        energy_gel_price_per_piece = 28.70
        pieces = 5
elif fruit == "Mango":
    if set_size == "small":
        energy_gel_price_per_piece = 36.66
        pieces = 2
    elif set_size == "big":
        energy_gel_price_per_piece = 19.60
        pieces = 5
elif fruit == "Pineapple":
    if set_size == "small":
        energy_gel_price_per_piece = 42.10
        pieces = 2
    elif set_size == "big":
        energy_gel_price_per_piece = 24.80
        pieces = 5
elif fruit == "Raspberry":
    if set_size == "small":
        energy_gel_price_per_piece = 20
        pieces = 2
    elif set_size == "big":
        energy_gel_price_per_piece = 15.20
        pieces = 5

total = energy_gel_price_per_piece * pieces * set_number

if total > 1000:
    total *= .50
elif total >= 400:
    total *= .85

print(f"{total:.2f} lv.")
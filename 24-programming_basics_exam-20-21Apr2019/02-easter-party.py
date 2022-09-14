number_of_guests = int(input())
cover_price_per_guest = float(input())
budget = float(input())

if number_of_guests > 20:
    cover_price_per_guest = cover_price_per_guest * .75
elif number_of_guests > 15:
    cover_price_per_guest = cover_price_per_guest * .8
elif number_of_guests >= 10:
    cover_price_per_guest = cover_price_per_guest * .85

cake_price = budget * .1

total = number_of_guests * cover_price_per_guest + cake_price

if total <= budget:
    remaining_money = budget - total
    print(f'It is party time! {remaining_money:.2f} leva left.')
else:
    missing_money = total - budget
    print(f'No party! {missing_money:.2f} leva needed.')
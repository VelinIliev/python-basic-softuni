from math import ceil

tennis_racket_price = float(input())
number_tennis_rackets = int(input())
pairs_snickers = int(input())

snickers_price = round(tennis_racket_price / 6, 2)

total_snickers_and_rackets = number_tennis_rackets * tennis_racket_price + pairs_snickers * snickers_price

other_equipment = round(total_snickers_and_rackets * .2,2)

total = total_snickers_and_rackets + other_equipment

djockovich_pay = total / 8
sponsors_pay = total - djockovich_pay

print(f'Price to be paid by Djokovic {int(djockovich_pay)}')
print(f'Price to be paid by sponsors {ceil(sponsors_pay)}')
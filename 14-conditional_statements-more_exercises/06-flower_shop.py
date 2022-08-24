from math import ceil

number_of_magnolias = int(input())
number_of_hyacinths = int(input())
number_of_roses = int(input())
number_of_cactuses = int(input())
price_of_gift = float(input())

magnolias_price = 3.25
hyacinths_price = 4
roses_price = 3.5
cactuses_price = 8

total = number_of_magnolias * magnolias_price + number_of_hyacinths * hyacinths_price + number_of_roses * roses_price + number_of_cactuses * cactuses_price
total_after_taxes = total * .95

if total_after_taxes >= price_of_gift:
    print(f'She is left with {int(total_after_taxes - price_of_gift)} leva.')
else:
    print(f'She will have to borrow {ceil(price_of_gift - total_after_taxes)} leva.')
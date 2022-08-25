number_of_chrysanthemums = int(input())
number_of_roses= int(input())
number_of_tulips= int(input())
season = input()
holiday = input()

if season == "Spring" or season == "Summer":
    chrysanthemum_price = 2.00
    rose_price = 4.10
    tulip_price = 2.50
elif season == "Autumn" or season == "Winter":
    chrysanthemum_price = 3.75
    rose_price = 4.50
    tulip_price = 4.15

boquet_price = number_of_chrysanthemums * chrysanthemum_price + number_of_roses * rose_price + number_of_tulips * tulip_price
if holiday == "Y":
    boquet_price *= 1.15
if number_of_tulips > 7 and season == "Spring":
    boquet_price *= .95
if number_of_roses >= 10 and season == "Winter":
    boquet_price *= .90
if number_of_roses + number_of_tulips + number_of_chrysanthemums > 20:
    boquet_price *= .80

bouquet_arranging_price = 2.00
boquet_price += bouquet_arranging_price

print(f'{boquet_price:.2f}')

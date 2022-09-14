destination = input()
period = input()
number_of_sleepover = int(input())

price_per_night = 0

if destination == "France":
    if period == "21-23":
        price_per_night = 30
    elif period == "24-27":
        price_per_night = 35
    elif period == "28-31":
        price_per_night = 40
elif destination == "Italy":
    if period == "21-23":
        price_per_night = 28
    elif period == "24-27":
        price_per_night = 32
    elif period == "28-31":
        price_per_night = 39
elif destination == "Germany":
    if period == "21-23":
        price_per_night = 32
    elif period == "24-27":
        price_per_night = 37
    elif period == "28-31":
        price_per_night = 43

total = number_of_sleepover * price_per_night

print(f'Easter trip to {destination} : {total:.2f} leva.')
budget = float(input())
season = input()

if budget > 1000:
    destination = "Europe"
    type_of_journey = "Hotel"
    price = budget * .9
elif budget > 100:
    destination = "Balkans"
    if season == "summer":
        type_of_journey = "Camp"
        price = budget * .4
    elif season == "winter":
        type_of_journey = "Hotel"
        price = budget *.8
else:
    destination = "Bulgaria"
    if season == "summer":
        type_of_journey = "Camp"
        price = budget * .3
    elif season == "winter":
        type_of_journey = "Hotel"
        price = budget *.7

print(f'Somewhere in {destination}')
print(f'{type_of_journey} - {price:.2f}')
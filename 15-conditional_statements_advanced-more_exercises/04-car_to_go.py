budget = float(input())
season = input()

if budget <= 100:
    car_class = "Economy class"
    if season == "Summer":
        car_type = "Cabrio"
        price = budget * .35
    else:
        car_type = "Jeep"
        price = budget * .65
elif budget <= 500:
    car_class = "Compact class"
    if season == "Summer":
        car_type = "Cabrio"
        price = budget * .45
    else:
        car_type = "Jeep"
        price = budget * .80
else:
    car_class = "Luxury class"
    car_type = "Jeep"
    price = budget * .90

print(f'{car_class}')
print(f'{car_type} - {price:.2f}')
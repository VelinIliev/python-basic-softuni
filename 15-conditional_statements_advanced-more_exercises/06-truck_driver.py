season = input()
km_per_month = float(input())

if season == "Spring" or season == "Autumn":
    if km_per_month <= 5000:
        price_per_km = .75
    elif km_per_month <= 10000:
        price_per_km = .95
    else:
        price_per_km = 1.45
elif season == "Summer":
    if km_per_month <= 5000:
        price_per_km = .90
    elif km_per_month <= 10000:
        price_per_km = 1.10
    else:
        price_per_km = 1.45
else:
    if km_per_month <= 5000:
        price_per_km = 1.05
    elif km_per_month <= 10000:
        price_per_km = 1.25
    else:
        price_per_km = 1.45

salary = km_per_month * 4 * price_per_km
salary_after_taxes = salary * .9

print(f'{salary_after_taxes:.2f}')
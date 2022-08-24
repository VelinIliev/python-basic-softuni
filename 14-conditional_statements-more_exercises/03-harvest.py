from math import ceil

vineyard_area = int(input())
grape_per_sq_m = float(input())
wine_needed = int(input())
number_workers = int(input())

total_grape = vineyard_area * grape_per_sq_m
grape_for_wine = total_grape * .4
wine_produced = grape_for_wine / 2.5

if wine_produced < wine_needed:
    diffrence = int(wine_needed - wine_produced)
    print(f'It will be a tough winter! More {diffrence} liters wine needed.')
elif wine_produced >= wine_needed:
    wine_on_top = ceil(wine_produced - wine_needed)
    wine_per_person = ceil(wine_on_top / number_workers)
    print(f'Good harvest this year! Total wine: {int(wine_produced)} liters.')
    print(f'{wine_on_top} liters left -> {wine_per_person} liters per person.')
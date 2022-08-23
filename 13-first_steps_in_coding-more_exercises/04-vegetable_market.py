vegetables_price_per_kg = float(input())
fruits_price_per_kg = float(input())
vegetables_kilograms = int(input())
fruits_kilograms = int(input())

total = vegetables_kilograms * vegetables_price_per_kg + fruits_kilograms * fruits_price_per_kg
total_euro = total / 1.94

print(f'{total_euro:.2f}')
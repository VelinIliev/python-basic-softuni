strawberries_price = float(input())
bananas_kg = float(input())
oranges_kg = float(input())
raspberries_kg = float(input())
strawberries_kg = float(input())

raspberries_price = strawberries_price / 2
oranges_price = raspberries_price * .6
bananas_price = raspberries_price * .2

total = strawberries_kg * strawberries_price + bananas_kg * bananas_price + oranges_kg * oranges_price + raspberries_kg * raspberries_price

print(f'{total:.2f}')
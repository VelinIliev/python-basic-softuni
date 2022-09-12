basketball_tax = int(input())

snickers_price = basketball_tax * .6
equip_price = snickers_price * .8
ball_price = equip_price / 4
accessories_price = ball_price / 5

total = basketball_tax + snickers_price + equip_price + ball_price + accessories_price

print(f'{total:.2f}')
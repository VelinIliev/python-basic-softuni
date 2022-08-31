budget = float(input())
number_of_extras = int(input())
costumes_price = float(input())

decor = budget * .1
extras_price = number_of_extras * costumes_price

if number_of_extras > 150:
    extras_price = extras_price * .9

if decor + extras_price > budget:
    print(f'Not enough money!')
    print(f'Wingard needs {decor + extras_price - budget:.2f} leva more.')
else:
    print(f'Action!')
    print(f'Wingard starts filming with {budget - decor - extras_price:.2f} leva left.')
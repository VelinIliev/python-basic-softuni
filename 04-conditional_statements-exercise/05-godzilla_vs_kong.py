budget = float(input())
walking_gentlemans = int(input())
costumes_price_per_piece = float(input())

decor = budget * .1

if walking_gentlemans > 150:
    costumes_price_per_piece *= .9

costumes_total = costumes_price_per_piece * walking_gentlemans

if costumes_total + decor > budget:
    not_enough_money = costumes_total + decor - budget
    print("Not enough money!")
    print(f'Wingard needs {not_enough_money:.2f} leva more.')
else:
    enough_money = budget - costumes_total - decor
    print("Action!")
    print(f'Wingard starts filming with {enough_money:.2f} leva left.')
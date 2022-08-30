budget = float(input())
number_of_overnights = int(input())
overnight_price = float(input())
percent_of_additional_costs = int(input())

if number_of_overnights > 7:
    overnight_price *= .95

vacation_cost = number_of_overnights * overnight_price + budget * (percent_of_additional_costs / 100)

if budget >= vacation_cost:
    print(f'Ivanovi will be left with {budget - vacation_cost:.2f} leva after vacation.')
else:
    print(f'{vacation_cost-budget:.2f} leva needed.')
budget = float(input())
category = input()
grour_size = int(input())

if grour_size <= 4:
    transport = budget * .75
elif grour_size <= 9:
    transport = budget * .6
elif grour_size <= 24:
    transport = budget * .5
elif grour_size <= 49:
    transport = budget * .4
elif grour_size > 50:
    transport = budget * .25

tickets_budget = budget - transport

if category == "VIP":
    ticket_price = 499.99
elif category == "Normal":
    ticket_price = 249.99

money_needed_for_tickets = ticket_price * grour_size

if tickets_budget >= money_needed_for_tickets:
    remaining_money = tickets_budget - money_needed_for_tickets
    print(f'Yes! You have {remaining_money:.2f} leva left.')
else:
    diffrence = money_needed_for_tickets - tickets_budget
    print(f'Not enough money! You need {diffrence:.2f} leva.')

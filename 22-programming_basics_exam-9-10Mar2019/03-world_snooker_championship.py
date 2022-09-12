championship_stage = input()
ticket_type = input()
number_of_tickets = int(input())
photo_with_trophy = input()

ticket_price = 0
photo_price = 40

if championship_stage == "Quarter final":
    if ticket_type == "Standard":
        ticket_price = 55.50
    elif ticket_type == "Premium":
        ticket_price = 105.20
    elif ticket_type == "VIP":
        ticket_price = 118.90
elif championship_stage == "Semi final":
    if ticket_type == "Standard":
        ticket_price = 75.88
    elif ticket_type == "Premium":
        ticket_price = 125.22
    elif ticket_type == "VIP":
        ticket_price = 300.40
elif championship_stage == "Final":
    if ticket_type == "Standard":
        ticket_price = 110.10
    elif ticket_type == "Premium":
        ticket_price = 160.66
    elif ticket_type == "VIP":
        ticket_price = 400.00

total_sum = ticket_price * number_of_tickets

if total_sum > 4000:
    total_sum *= .75
    photo_price = 0
elif total_sum > 2500:
    total_sum *= .9

if photo_with_trophy == "Y":
    total_sum += number_of_tickets * photo_price

print(f'{total_sum:.2f}')
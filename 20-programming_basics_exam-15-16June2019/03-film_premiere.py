projection_type = input()
packet_type = input()
number_of_tickets = int(input())

ticket_price = 0

if projection_type == "John Wick":
    if packet_type == "Drink":
        ticket_price = 12
    elif packet_type == "Popcorn":
        ticket_price = 15
    elif packet_type == "Menu":
        ticket_price = 19
elif projection_type == "Star Wars":
    if packet_type == "Drink":
        ticket_price = 18
    elif packet_type == "Popcorn":
        ticket_price = 25
    elif packet_type == "Menu":
        ticket_price = 30
elif projection_type == "Jumanji":
    if packet_type == "Drink":
        ticket_price = 9
    elif packet_type == "Popcorn":
        ticket_price = 11
    elif packet_type == "Menu":
        ticket_price = 14

if projection_type == "Star Wars" and number_of_tickets >= 4:
    ticket_price *= .7
if projection_type and number_of_tickets == 2:
    ticket_price *= .85

total = ticket_price * number_of_tickets

print(f'Your bill is {total:.2f} leva.')
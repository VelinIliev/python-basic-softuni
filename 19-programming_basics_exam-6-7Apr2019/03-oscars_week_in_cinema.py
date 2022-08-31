movie_name = input()
hall_type = input()
number_of_tickets = int(input())
ticket_price = 0

if movie_name == "A Star Is Born":
    if hall_type == "normal":
        ticket_price = 7.50
    elif hall_type == "luxury":
        ticket_price = 10.50
    elif hall_type == "ultra luxury":
        ticket_price = 13.50
elif movie_name == "Bohemian Rhapsody":
    if hall_type == "normal":
        ticket_price = 7.35
    elif hall_type == "luxury":
        ticket_price = 9.45
    elif hall_type == "ultra luxury":
        ticket_price = 12.75
elif movie_name == "Green Book":
    if hall_type == "normal":
        ticket_price = 8.15
    elif hall_type == "luxury":
        ticket_price = 10.25
    elif hall_type == "ultra luxury":
        ticket_price = 13.25
elif movie_name == "The Favourite":
    if hall_type == "normal":
        ticket_price = 8.75
    elif hall_type == "luxury":
        ticket_price = 11.55
    elif hall_type == "ultra luxury":
        ticket_price = 13.95

total = number_of_tickets * ticket_price

print(f'{movie_name} -> {total:.2f} lv.')
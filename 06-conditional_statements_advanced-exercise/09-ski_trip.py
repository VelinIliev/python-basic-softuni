days_of_vacation = int(input())
room_type = input()
rating = input()

room_for_one = 18
apartment = 25
president_appartment = 35
overnights = days_of_vacation - 1

if overnights < 10:
    if room_type == "room for one person":
        price = overnights * room_for_one
    elif room_type == "apartment":
        price = (overnights * apartment) * .7
    elif room_type == "president apartment":
        price = (overnights * president_appartment) * .9
elif overnights <= 15:
    if room_type == "room for one person":
        price = overnights * room_for_one
    elif room_type == "apartment":
        price = (overnights * apartment) * .65
    elif room_type == "president apartment":
        price = (overnights * president_appartment) * .85
elif overnights > 15:
    if room_type == "room for one person":
        price = overnights * room_for_one
    elif room_type == "apartment":
        price = (overnights * apartment) * .5
    elif room_type == "president apartment":
        price = (overnights * president_appartment) * .8

if rating == "positive":
    price = price * 1.25
elif rating == "negative":
    price = price * .9

print(f'{price:.2f}')
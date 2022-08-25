season = input()
group_type = input()
number_of_students = int(input())
number_of_overnight = int(input())

if season == "Winter":
    if group_type == "boys":
        price_per_person = 9.60
        sport_type = "Judo"
    elif group_type == "girls":
        price_per_person = 9.60
        sport_type = "Gymnastics"
    elif group_type == "mixed":
        price_per_person = 10.00
        sport_type = "Ski"
elif season == "Spring":
    if group_type == "boys":
        sport_type = "Tennis"
        price_per_person = 7.20
    elif group_type == "girls":
        price_per_person = 7.20
        sport_type = "Athletics"
    elif group_type == "mixed":
        price_per_person = 9.50
        sport_type = "Cycling"
elif season == "Summer":
    if group_type == "boys":
        price_per_person = 15.00
        sport_type = "Football"
    elif group_type == "girls":
        price_per_person = 15.00
        sport_type = "Volleyball"
    elif group_type == "mixed":
        price_per_person = 20.00
        sport_type = "Swimming"

total = price_per_person * number_of_students * number_of_overnight

if 10 <= number_of_students < 20:
    total *= .95
elif 20 <= number_of_students < 50:
    total *= .85
elif number_of_students >= 50:
    total *= .50

print(f'{sport_type} {total:.2f} lv.')
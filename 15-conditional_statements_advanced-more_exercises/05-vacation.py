budget = float(input())
season = input()

if budget <= 1000:
    type_of_vacation = "Camp"
    if season == "Summer":
        destination = "Alaska"
        price = budget * .65
    else:
        destination = "Morocco"
        price = budget * .45
elif budget <= 3000:
    type_of_vacation = "Hut"
    if season == "Summer":
        destination = "Alaska"
        price = budget * .80
    else:
        destination = "Morocco"
        price = budget * .60
else:
    type_of_vacation = "Hotel"
    price = budget * .90
    if season == "Summer":
        destination = "Alaska"
    else:
        destination = "Morocco"

print(f'{destination} - {type_of_vacation} - {price:.2f}')

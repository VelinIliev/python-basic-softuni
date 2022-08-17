budjet = int(input())
season = input()
number_of_fishermans = int(input())

boat_rent = 0

if season == "Spring":
    boat_rent = 3000
elif season == "Summer":
    boat_rent = 4200
elif season == "Autumn":
    boat_rent = 4200
elif season == "Winter":
    boat_rent = 2600

if number_of_fishermans <= 6:
    boat_rent = boat_rent * 0.9
elif number_of_fishermans <= 11:
    boat_rent = boat_rent * 0.85
else:
    boat_rent = boat_rent * 0.75

if number_of_fishermans % 2 == 0 and season != "Autumn":
    boat_rent = boat_rent * .95

if budjet >= boat_rent:
    remaining_money = budjet - boat_rent
    print(f'Yes! You have {remaining_money:.2f} leva left.')
else:
    needed_money = boat_rent - budjet
    print(f'Not enough money! You need {needed_money:.2f} leva.')
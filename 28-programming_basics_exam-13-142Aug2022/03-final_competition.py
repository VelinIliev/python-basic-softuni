number_of_dancers = int(input())
points = float(input())
season = input()
place = input()

award = 0

if place == "Bulgaria":
    award = points * number_of_dancers
    if season == "summer":
        award *= .95
    elif season == "winter":
        award *= .92
elif place == "Abroad":
    award = (points * number_of_dancers) * 1.5
    if season == "summer":
        award *= .90
    elif season == "winter":
        award *= .85

donation = award * .75
print(f'Charity - {donation:.2f}')

money_per_dencer = (award - donation) / number_of_dancers
print(f'Money per dancer - {money_per_dencer:.2f}')
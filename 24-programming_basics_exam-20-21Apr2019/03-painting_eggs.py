eggs_size = input()
eggs_color = input()
number_of_lots = int(input())

egg_lots_price = 0

if eggs_size == "Large":
    if eggs_color == "Red":
        egg_lots_price = 16
    elif eggs_color == "Green":
        egg_lots_price = 12
    elif eggs_color == "Yellow":
        egg_lots_price = 9
elif eggs_size == "Medium":
    if eggs_color == "Red":
        egg_lots_price = 13
    elif eggs_color == "Green":
        egg_lots_price = 9
    elif eggs_color == "Yellow":
        egg_lots_price = 7
elif eggs_size == "Small":
    if eggs_color == "Red":
        egg_lots_price = 9
    elif eggs_color == "Green":
        egg_lots_price = 8
    elif eggs_color == "Yellow":
        egg_lots_price = 5

income = number_of_lots * egg_lots_price
expenses = income * .35

profit = income - expenses

print(f'{profit:.2f} leva.')
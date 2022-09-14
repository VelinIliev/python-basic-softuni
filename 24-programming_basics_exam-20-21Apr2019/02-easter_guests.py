from math import ceil

number_of_guests = int(input())
budget = int(input())

number_of_easter_breads = int(ceil(number_of_guests / 3))
number_of_eggs = number_of_guests * 2

easter_bread_price = 4
egg_price = .45

total_easter_breads = number_of_easter_breads * easter_bread_price
total_eggs = number_of_eggs * egg_price

total = total_eggs + total_easter_breads

if total <= budget:
    remaining_money = budget - total
    print(f'Lyubo bought {number_of_easter_breads} Easter bread and {number_of_eggs} eggs.')
    print(f'He has {remaining_money:.2f} lv. left.')
else:
    missing_money = total - budget
    print(f"Lyubo doesn't have enough money.")
    print(f'He needs {missing_money:.2f} lv. more.')
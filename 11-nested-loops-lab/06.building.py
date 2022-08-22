number_of_floors = int(input())
number_of_rooms = int(input())

for floor in range(number_of_floors, 0, -1):
    for room in range(0, number_of_rooms):
        if floor == number_of_floors:
            print(f'L{floor}{room}', end = " ")
        elif floor % 2 == 0:
            print(f'O{floor}{room}', end=" ")
        else:
            print(f'A{floor}{room}', end=" ")
    print()
player_name = input()
starting_points = 301
player_points = starting_points
count_shots = 0
unsuccessful_shots = 0

while True:
    field = input()

    if field == "Retire":
        print(f'{player_name} retired after {unsuccessful_shots} unsuccessful shots.')
        break

    points = int(input())

    current_points = 0

    if field == "Single":
        current_points += points
        count_shots += 1
    elif field == "Double":
        current_points += points * 2
        count_shots += 1
    elif field == "Triple":
        current_points += points * 3
        count_shots += 1
    player_points -= current_points

    if player_points == 0:
        print(f'{player_name} won the leg with {count_shots} shots.')
        break
    elif player_points < 0:
        player_points += current_points
        unsuccessful_shots += 1
        count_shots -= 1

number_of_easter_breads = int(input())

max_points = 0
winner = ""

for easter_bread in range(number_of_easter_breads):
    baker = input()
    total_points = 0
    while True:
        points = input()
        if points == "Stop":
            print(f'{baker} has {total_points} points.')
            break
        else:
            points = int(points)
            total_points += points

    if total_points > max_points:
        max_points = total_points
        winner = baker
        print(f'{baker} is the new number 1!')

print(f'{winner} won competition with {max_points} points!')
number_of_tournaments = int(input())
starting_points = int(input())

points = starting_points
count_w = 0


for x in range(number_of_tournaments):
    position = input()
    if position == "W":
        points += 2000
        count_w += 1
    elif position == "F":
        points += 1200
    elif position == "SF":
        points += 720

average_points = (points - starting_points) / number_of_tournaments
wins_pecent = count_w / number_of_tournaments * 100

print(f'Final points: {points}')
print(f'Average points: {int(average_points)}')
print(f'{wins_pecent:.2f}%')
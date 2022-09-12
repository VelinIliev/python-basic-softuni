number_of_tournaments = int(input())
stating_points = int(input())

tournaments_won = 0
final_points = stating_points

for tournament in range(number_of_tournaments):
    ranked = input()
    if ranked == "W":
        final_points += 2000
        tournaments_won += 1
    elif ranked == "F":
        final_points += 1200
    elif ranked == "SF":
        final_points += 720

print(f'Final points: {final_points}')
print(f'Average points: {int((final_points - stating_points) / number_of_tournaments)}')
print(f'{tournaments_won / number_of_tournaments * 100:.2f}%')
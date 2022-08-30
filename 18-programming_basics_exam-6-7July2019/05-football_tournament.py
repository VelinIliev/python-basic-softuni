team_name = input()
number_of_matches = int(input())

total_points = 0
wins = 0
draws = 0
loses = 0

for match in range(number_of_matches):
    match_result = input()
    if match_result == "W":
        wins += 1
        total_points += 3
    elif match_result == "D":
        draws += 1
        total_points += 1
    elif match_result == "L":
        loses += 1

if number_of_matches == 0:
    print(f"{team_name} hasn't played any games during this season.")
else:
    print(f'{team_name} has won {total_points} points during this season.')
    print("Total stats:")
    print(f"## W: {wins}")
    print(f"## D: {draws}")
    print(f"## L: {loses}")
    print(f'Win rate: {wins / number_of_matches * 100:.2f}%')
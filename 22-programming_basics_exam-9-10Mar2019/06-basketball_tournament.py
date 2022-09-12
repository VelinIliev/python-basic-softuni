wins = 0
lose = 0
matches_counter = 0

while True:
    tournament_name = input()
    if tournament_name == "End of tournaments":
        print(f'{wins / matches_counter * 100:.2f}% matches win')
        print(f'{lose / matches_counter * 100:.2f}% matches lost')
        break
    number_of_matches = int(input())

    for match in range(number_of_matches):
        desi_team_points = int(input())
        other_team_points = int(input())
        matches_counter += 1

        if desi_team_points > other_team_points:
            print(f'Game {match+1} of tournament {tournament_name}: win with {desi_team_points - other_team_points} points.')
            wins += 1
        elif desi_team_points < other_team_points:
            print(f'Game {match+1} of tournament {tournament_name}: lost with {other_team_points - desi_team_points} points.')
            lose += 1
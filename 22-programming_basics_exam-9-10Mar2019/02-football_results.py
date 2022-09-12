first_match_results = input()
second_match_results = input()
third_match_results = input()

wins = 0
draws = 0
lost = 0

if first_match_results[0] > first_match_results[-1]:
    wins += 1
elif first_match_results[0] == first_match_results[-1]:
    draws += 1
else:
    lost += 1

if second_match_results[0] > second_match_results[-1]:
    wins += 1
elif second_match_results[0] == second_match_results[-1]:
    draws += 1
else:
    lost += 1

if third_match_results[0] > third_match_results[-1]:
    wins += 1
elif third_match_results[0] == third_match_results[-1]:
    draws += 1
else:
    lost += 1

print(f'Team won {wins} games.')
print(f'Team lost {lost} games.')
print(f'Drawn games: {draws}')
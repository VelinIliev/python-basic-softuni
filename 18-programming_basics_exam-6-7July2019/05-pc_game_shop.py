number_of_games_sold = int(input())

hearthstone = 0
fornite = 0
overwatch = 0
others = 0

for game in range(number_of_games_sold):
    game_name = input()
    if game_name == "Hearthstone":
        hearthstone += 1
    elif game_name == "Fornite":
        fornite += 1
    elif game_name == "Overwatch":
        overwatch += 1
    else:
        others += 1

print(f'Hearthstone - {hearthstone / number_of_games_sold * 100:.2f}%')
print(f'Fornite - {fornite / number_of_games_sold * 100:.2f}%')
print(f'Overwatch - {overwatch / number_of_games_sold * 100:.2f}%')
print(f'Others - {others / number_of_games_sold * 100:.2f}%')
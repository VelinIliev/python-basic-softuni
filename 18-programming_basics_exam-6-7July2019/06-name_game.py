# print(ord("I"))
# print(chr(97))
winner_points = 0
winner_name = ""

while True:
    player_name = input()

    if player_name == "Stop":
        print(f'The winner is {winner_name} with {winner_points} points!')
        break

    current_points = 0

    for letter in player_name:
        number = int(input())
        if number == ord(letter):
            current_points += 10
        else:
            current_points += 2

    if current_points >= winner_points:
        winner_points = current_points
        winner_name = player_name
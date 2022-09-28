tournaments = int(input())

money_for_charity = 0
total_win_days = 0
total_lose_days = 0

for day in range(tournaments):
    daily_money = 0
    daily_wins = 0
    daily_loses = 0
    while True:
        command = input()
        if command == "Finish":
            break
        else:
            sport = command
            result = input()
        if result == "win":
            daily_money += 20
            daily_wins += 1
        elif result == "lose":
            daily_loses += 1
    if daily_wins > daily_loses:
        daily_money *= 1.1
        total_win_days += 1
    else:
        total_lose_days += 1
    money_for_charity += daily_money

if total_win_days > total_lose_days:
    money_for_charity *= 1.2
    print(f'You won the tournament! Total raised money: {money_for_charity:.2f}')
else:
    print(f'You lost the tournament! Total raised money: {money_for_charity:.2f}')
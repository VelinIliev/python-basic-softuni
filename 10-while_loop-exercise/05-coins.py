change = int(float(input())*100)

coins = [200, 100, 50, 20, 10, 5, 2, 1]
count_coins = 0

while change > 0:
    if change // coins[0] > 0:
        count_coins += 1
        change = change - 200
    elif change // coins[1] > 0:
        count_coins += 1
        change = change - 100
    elif change // coins[2] > 0:
        count_coins += 1
        change = change - 50
    elif change // coins[3] > 0:
        count_coins += 1
        change = change - 20
    elif change // coins[4] > 0:
        count_coins += 1
        change = change - 10
    elif change // coins[5] > 0:
        count_coins += 1
        change = change - 5
    elif change // coins[6] > 0:
        count_coins += 1
        change = change - 2
    elif change // coins[7] > 0:
        count_coins += 1
        change = change - 1

print(count_coins)
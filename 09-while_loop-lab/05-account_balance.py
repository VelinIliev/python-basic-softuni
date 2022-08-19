account_balance = 0

while True:
    new_money = input()
    if new_money == "NoMoreMoney":
        break
    else:
        new_money = float(new_money)
        if new_money < 0:
            print(f'Invalid operation!')
            break
        else:
            account_balance += new_money
            print(f'Increase: {new_money:.2f}')

print(f'Total: {account_balance:.2f}')
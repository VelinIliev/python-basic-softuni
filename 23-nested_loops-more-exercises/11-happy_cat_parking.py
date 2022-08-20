days = int(input())
hours = int(input())

total_price = 0

for day in range(1, days + 1):
    current_price = 0
    for hour in range(1, hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            current_price += 2.5
        elif day % 2 != 0 and hour % 2 == 0:
            current_price += 1.25
        else:
            current_price += 1

    print(f'Day: {day} - {current_price:.2f} leva')
    total_price += current_price

print(f'Total: {total_price:.2f} leva')

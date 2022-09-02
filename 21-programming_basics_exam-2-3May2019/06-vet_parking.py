number_of_days = int(input())
number_of_hours = int(input())

total_price = 0

for day in range(1, number_of_days + 1):
    current_price = 0
    for hour in range(1, number_of_hours + 1):
        if day % 2 == 0 and hour % 2 != 0:
            price = 2.50
        elif day % 2 != 0 and hour % 2 == 0:
            price =  1.25
        else:
            price = 1
        current_price += price
    print(f'Day: {day} - {current_price:.2f} leva')
    total_price += current_price

print(f'Total: {total_price:.2f} leva')
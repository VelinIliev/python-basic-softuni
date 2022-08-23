number = int(input())

for x in range(1111, 10000):
    is_special_number = 0
    for digit in str(x):
        digit = int(digit)
        if digit == 0:
            pass
        elif number % digit == 0:
            is_special_number += 1
    if is_special_number == 4:
        print(x, end = " ")

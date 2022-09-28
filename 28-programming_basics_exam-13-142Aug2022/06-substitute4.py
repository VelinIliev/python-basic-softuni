k = int(input())
l = int(input())
m = int(input())
n = int(input())
substitutes = 0

for first_digit in range(k, 9):
    if substitutes == 6:
        break
    elif first_digit % 2 != 0:
        continue
    for second_digit in range(9, l - 1, -1):
        if substitutes == 6:
            break
        elif second_digit % 2 == 0:
            continue
        first_number = int(str(first_digit) + str(second_digit))
        for third_digit in range(m, 9):
            if substitutes == 6:
                break
            elif third_digit % 2 != 0:
                continue
            for forth_digit in range(9, n - 1, -1):
                if substitutes == 6:
                    break
                elif forth_digit % 2 == 0:
                    continue
                second_number = int(str(third_digit) + str(forth_digit))
                if first_number == second_number:
                    print("Cannot change the same player.")
                else:
                    print(f'{first_number} - {second_number}')
                    substitutes += 1
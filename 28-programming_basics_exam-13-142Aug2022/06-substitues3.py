k = int(input())
l = int(input())
m = int(input())
n = int(input())

substitutes_count = 0

for first_digit in range(k, 8 + 1):
    for second_digit in range(9, l - 1, -1):
        if first_digit % 2 == 0 and second_digit % 2 != 0:
            first_number = int(str(first_digit) + str(second_digit))
            for third_digit in range(m, 8 + 1):
                for forth_digit in range(9, n - 1, -1):
                    if third_digit % 2 == 0 and forth_digit % 2 != 0:
                        second_number = int(str(third_digit) + str(forth_digit))
                        if substitutes_count == 6:
                            break
                        elif first_number == second_number:
                            print("Cannot change the same player.")
                        elif first_number != second_number:
                            print(f'{first_number} - {second_number}')
                            substitutes_count += 1

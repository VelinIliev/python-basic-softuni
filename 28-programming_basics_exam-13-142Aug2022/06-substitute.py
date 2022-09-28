k = int(input())
l = int(input())
m = int(input())
n = int(input())
substitutes = 0

for first_digit_of_first_number in range(k, 8 + 1):
    for second_digit_of_first_number in range(9, l-1, -1):
        if first_digit_of_first_number % 2 == 0 and second_digit_of_first_number % 2 != 0:
            for first_digit_of_second_number in range(m, 8 + 1):
                for second_digit_of_second_number in range(9, n-1, -1):
                    if first_digit_of_second_number % 2 == 0 and second_digit_of_second_number % 2 != 0:
                        first_number = int(str(first_digit_of_first_number) + str(second_digit_of_first_number))
                        second_number = int(str(first_digit_of_second_number) + str(second_digit_of_second_number))
                        if substitutes >= 6:
                            break
                        if first_number == second_number:
                            print(f'Cannot change the same player.')
                        elif first_number != second_number:
                            substitutes += 1
                            print(f'{first_number} - {second_number}')

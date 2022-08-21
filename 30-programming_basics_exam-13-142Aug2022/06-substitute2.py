k = int(input())
l = int(input())
m = int(input())
n = int(input())

substitutes_count = 0

if 0 <= k <= 8 and 0 <= l <= 9 and 0 <= m <= 8 and 0 <= n <= 9:
    for first_digit_first_number in range(k, 8 + 1):
        if first_digit_first_number % 2 == 0:
            for second_digit_first_number in range(9, l - 1, -1):
                if second_digit_first_number % 2 != 0:
                    first_number = int(str(first_digit_first_number) + str(second_digit_first_number))
                    for first_digit_second_number in range(m, 8 + 1):
                        if first_digit_second_number % 2 == 0:
                            for second_digit_second_number in range(9, n - 1, -1):
                                if second_digit_second_number % 2 != 0:
                                    second_number = int(str(first_digit_second_number) + str(second_digit_second_number))
                                    if substitutes_count >= 6:
                                        break
                                    else:
                                        if first_number != second_number:
                                            print(f'{first_number} - {second_number}')
                                            substitutes_count += 1
                                        else:
                                            print('Cannot change the same player.')

number = int(input())

for first_digit in range(1, 10):
    for second_digit in range(1, 10):
        first_sum = first_digit + second_digit
        if number % first_sum == 0:
            for third_digit in range(1, 10):
                for forth_digit in range(1, 10):
                    second_sum = third_digit + forth_digit
                    if first_sum == second_sum:
                        print(f'{first_digit}{second_digit}{third_digit}{forth_digit}', end = " ")
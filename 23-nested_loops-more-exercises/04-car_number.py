start = int(input())
end = int(input())

for first_digit in range(start, end + 1):
    for second_digit in range(start, end + 1):
        for third_digit in range(start, end + 1):
            if (second_digit + third_digit) % 2 == 0:
                for forth_digit in range (start, end + 1):
                    if (first_digit % 2 == 0 and forth_digit % 2 != 0) or (first_digit % 2 != 0 and forth_digit % 2 == 0):
                        if first_digit > forth_digit:
                            print(f'{first_digit}{second_digit}{third_digit}{forth_digit}', end = " ")

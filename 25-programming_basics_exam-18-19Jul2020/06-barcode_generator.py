barcode_start = int(input())
barcode_end = int(input())

first_digit_start = int(str(barcode_start)[0])
first_digit_end = int(str(barcode_end)[0])

second_digit_start = int(str(barcode_start)[1])
second_digit_end = int(str(barcode_end)[1])

third_digit_start = int(str(barcode_start)[2])
third_digit_end = int(str(barcode_end)[2])

forth_digit_start = int(str(barcode_start)[3])
forth_digit_end = int(str(barcode_end)[3])


for first_digit in range(first_digit_start, first_digit_end + 1):
    if first_digit % 2 == 0:
        continue
    for second_digit in range(second_digit_start, second_digit_end + 1):
        if second_digit % 2 == 0:
            continue
        for third_digit in range(third_digit_start, third_digit_end + 1):
            if third_digit % 2 == 0:
                continue
            for forth_digit in range(forth_digit_start, forth_digit_end + 1):
                if forth_digit % 2 == 0:
                    continue
                print(f'{first_digit}{second_digit}{third_digit}{forth_digit}', end = " ")

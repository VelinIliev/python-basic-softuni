max_hundreds = int(input())
max_tens = int(input())
max_ones = int(input())

for hundred in range(1, max_hundreds + 1):
    if hundred % 2 != 0:
        continue
    for ten in range(1, max_tens + 1):
        if ten == 1 or ten == 4 or ten == 6 or ten == 8 or ten == 9:
            continue
        for one in range(1, max_ones + 1):
            if one % 2 != 0:
                continue
            print(f'{hundred} {ten} {one}')
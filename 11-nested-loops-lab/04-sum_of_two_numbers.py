interval_start = int(input())
interval_end = int(input())
magic_number = int(input())

count_itterations = 0
found_magic_number = False

for x1 in range(interval_start, interval_end+1):
    for x2 in range(interval_start, interval_end+1):
        count_itterations += 1
        if x1 + x2 == magic_number:
            print(f'Combination N:{count_itterations} ({x1} + {x2} = {magic_number})')
            found_magic_number = True
            break
    else:
        continue
    break
if found_magic_number == False:
    print(f'{count_itterations} combinations - neither equals {magic_number}')

start = int(input())
end = int(input())
magic_number = int(input())
position = 0
magic_number_found = False

for first_digit in range(start, end + 1):
    for second_digit in range(start, end + 1):
        position += 1
        if first_digit + second_digit == magic_number:
            print(f"Combination N:{position} ({first_digit} + {second_digit} = {magic_number})")
            magic_number_found = True
            break
    if first_digit + second_digit == magic_number:
        break

if not magic_number_found:
    print(f'{position} combinations - neither equals {magic_number}')
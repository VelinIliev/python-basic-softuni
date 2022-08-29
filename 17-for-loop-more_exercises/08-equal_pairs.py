number_of_pairs = int(input())

sum_to_check = 0
is_all_equal = 0
max_difference = 0

for number in range(number_of_pairs):
    first_number = int(input())
    second_number = int(input())
    if number == 0:
        sum_to_check = first_number + second_number
        is_all_equal += 1
    else:
        if sum_to_check == first_number + second_number:
            is_all_equal += 1

        max_difference_checker = abs(sum_to_check - (first_number + second_number))

        if max_difference_checker > max_difference:
            max_difference = max_difference_checker

        sum_to_check = first_number + second_number

if is_all_equal == number_of_pairs:
    print(f"Yes, value={sum_to_check}")
else:
    print(f'No, maxdiff={max_difference}')
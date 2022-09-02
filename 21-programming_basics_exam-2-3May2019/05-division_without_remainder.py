number_of_numbers = int(input())
division_by_2 = 0
division_by_3 = 0
division_by_4 = 0

for number in range(number_of_numbers):
    test_number = int(input())
    if test_number % 2 == 0:
        division_by_2 += 1
    if test_number % 3 == 0:
        division_by_3 += 1
    if test_number % 4 == 0:
        division_by_4 += 1

print(f'{division_by_2 / number_of_numbers * 100:.2f}%')
print(f'{division_by_3 / number_of_numbers * 100:.2f}%')
print(f'{division_by_4 / number_of_numbers * 100:.2f}%')
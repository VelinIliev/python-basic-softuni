iterations = int(input())

numbers = []

for x in range(iterations):
    number = int(input())
    numbers.append(number)

sum = 0
count_max = 0

for number in numbers:
    if number == max(numbers) and count_max == 0:
        count_max += 1
    else:
        sum += number

if sum == max(numbers):
    print("Yes")
    print(f'Sum = {sum}')
else:
    diffrence = abs(max(numbers) - sum)
    print("No")
    print(f'Diff = {diffrence}')
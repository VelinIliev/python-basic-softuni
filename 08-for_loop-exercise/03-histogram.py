iterations = int(input())

numbers = []

for x in range(iterations):
    number = int(input())
    numbers.append(number)

count_to_199 = 0
count_to_399 = 0
count_to_599 = 0
count_to_799 = 0
count_to_1000 = 0

for number in numbers:
    if number < 200:
        count_to_199 += 1
    elif number < 400:
        count_to_399 += 1
    elif number < 600:
        count_to_599 += 1
    elif number < 800:
        count_to_799 += 1
    else:
        count_to_1000 += 1

print(f'{(count_to_199 / len(numbers) * 100):.2f}%')
print(f'{(count_to_399 / len(numbers) * 100):.2f}%')
print(f'{(count_to_599 / len(numbers) * 100):.2f}%')
print(f'{(count_to_799 / len(numbers) * 100):.2f}%')
print(f'{(count_to_1000 / len(numbers) * 100):.2f}%')
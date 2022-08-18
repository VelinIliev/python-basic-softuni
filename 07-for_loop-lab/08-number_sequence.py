iterations = int(input())

numbers = []

for x in range(iterations):
    number = int(input())
    numbers.append(number)

max_number = max(numbers)
min_number = min(numbers)

print(f'Max number: {max_number}')
print(f'Min number: {min_number}')
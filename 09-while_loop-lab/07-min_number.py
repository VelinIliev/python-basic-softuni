numbers = []

while True:
    entry = input()
    if entry == "Stop":
        break
    else:
        entry = int(entry)
        numbers.append(entry)

min_number = 1000000000000

for number in numbers:
    if number < min_number:
        min_number = number

print(min_number)

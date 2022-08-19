numbers = []

while True:
    entry = input()
    if entry == "Stop":
        break
    else:
        entry = int(entry)
        numbers.append(entry)

max_number = -1000000000000

for number in numbers:
    if number > max_number:
        max_number = number

print(max_number)

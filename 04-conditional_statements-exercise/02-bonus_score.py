number = int(input())

if number <= 100:
    bonus = number + 5
elif number < 1000:
    bonus = number + number * .2
else:
    bonus = number + number * .1

if number % 2 == 0:
    bonus += 1

lastdigit = int(repr(number)[-1])

if lastdigit == 5:
    bonus += 2

bonus_points = round(bonus - number, 1)

print(bonus_points)
print(bonus)
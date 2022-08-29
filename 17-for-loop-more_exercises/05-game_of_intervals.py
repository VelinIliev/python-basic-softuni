number_of_moves = int(input())
result = 0

invalid = 0
from_0_to_9 = 0
from_10_to_19 = 0
from_20_to_29 = 0
from_30_to_39 = 0
from_40_to_50 = 0

for move in range(number_of_moves):
    number = int(input())
    if number < 0 or number > 50:
        result = result / 2
        invalid += 1
    elif number < 10:
        result += number * .2
        from_0_to_9 += 1
    elif number < 20:
        result += number * .3
        from_10_to_19 += 1
    elif number < 30:
        result += number * .4
        from_20_to_29 += 1
    elif number < 40:
        result += 50
        from_30_to_39 += 1
    elif number <= 50:
        result += 100
        from_40_to_50 += 1

print(f'{result:.2f}')
print(f'From 0 to 9: {from_0_to_9 / number_of_moves * 100:.2f}%')
print(f'From 10 to 19: {from_10_to_19 / number_of_moves * 100:.2f}%')
print(f'From 20 to 29: {from_20_to_29 / number_of_moves * 100:.2f}%')
print(f'From 30 to 39: {from_30_to_39 / number_of_moves * 100:.2f}%')
print(f'From 40 to 50: {from_40_to_50 / number_of_moves * 100:.2f}%')
print(f'Invalid numbers: {invalid / number_of_moves * 100:.2f}%')

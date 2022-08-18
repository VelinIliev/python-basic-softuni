iterations = int(input())
left_sum = 0
right_sum = 0

for x in range(iterations):
    number = int(input())
    left_sum += number

for x in range(iterations):
    number = int(input())
    right_sum += number

if right_sum == left_sum:
    print(f'Yes, sum = {left_sum}')
else:
    diffrence = abs(left_sum - right_sum)
    print(f'No, diff = {diffrence}')
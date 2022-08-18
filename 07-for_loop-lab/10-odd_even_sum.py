iteraions = int(input())

even_sum = 0
odd_sum = 0

for x in range(iteraions):
    number = int(input())
    if x % 2 == 0:
        even_sum += number
    else:
        odd_sum += number

if even_sum == odd_sum:
    print("Yes")
    print(f'Sum = {even_sum}')
else:
    diffrence = abs (even_sum - odd_sum)
    print("No")
    print(f"Diff = {diffrence}")
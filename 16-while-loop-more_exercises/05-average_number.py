n = int(input())
sum = 0
for number in range(n):
    digit = int(input())
    sum += digit

print(f'{sum / n:.2f}')
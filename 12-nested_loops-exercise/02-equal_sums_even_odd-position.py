start = int(input())
end = int(input())

for number in range(start, end + 1):
    odd_sum = 0
    even_sum = 0
    n = 0

    for digit in str(number):
        n = n + 1
        if n % 2 != 0:
            odd_sum += int(digit)
        else:
            even_sum += int(digit)

    if odd_sum == even_sum:
        print(f'{number}', end = ' ')

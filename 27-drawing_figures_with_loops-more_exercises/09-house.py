from math import ceil
n = int(input())

for x in range(1, int((n + 1) / 2) + 1):

    if x == 1:
        if n % 2 == 0:
            print("-" * int((n / 2 - 1)) + "**" + "-" * int((n / 2 - 1)))
        else:
            print("-" * int((n / 2)) + "*" + "-" * int((n / 2)))
    else:
        if n % 2 == 0:
            print("-" * int((n - 2 * x) / 2) + "*" * (x * 2) + "-" * int((n - 2 * x) / 2))
        else:
            print("-" * ceil(n / 2 - x) + "*" * (x * 2 - 1) + "-" * ceil(n / 2 - x))

for y in range(1, int(n / 2) + 1):
    print("|" + "*" * (n - 2) + "|")

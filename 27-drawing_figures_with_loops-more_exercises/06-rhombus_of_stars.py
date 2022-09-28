n = int(input())

for x in range(1, n + 1):
    print(' ' * (n - x) + "* " * x + ' ' * (n - x))

for y in range(n - 1, 0, -1):
    print(' ' * (n-y) + "* " * y + ' ' * (n-y))

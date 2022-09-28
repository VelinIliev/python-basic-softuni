n = int(input())

for x in range(0, n + 1):
    print(" " * (n - x) + "*" * x + " | " + "*" * x + " " * (n - x))

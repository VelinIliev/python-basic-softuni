n = int(input())

for x in range(1, n + 1):
    if x == 1 or x == (n):
        print("+ " + "- " * (n - 2) + "+", end = "")
    else:
        print("| " + "- " * (n - 2) + "|", end = "")
    print()
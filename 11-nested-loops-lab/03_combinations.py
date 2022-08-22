n = int(input())

count_solutions = 0

for x1 in range(0,n+1):
    for x2 in range(0, n+1):
        for x3 in range(0, n+1):
            result = x1 + x2 + x3
            if result == n:
                count_solutions += 1

print(count_solutions)
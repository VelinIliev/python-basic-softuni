n = int(input())

for x in range(1, int((n + 1) / 2)):

    if x == 1 and n % 2 == 0:
        print('-' * (int((n-1)/2)) + "**" + '-' * (int((n-1)/2)))
    elif x == 1 and n % 2 != 0:
        print('-' * (int((n - 1) / 2)) + "*" + '-' * (int((n - 1) / 2)))

    if n % 2 != 0 :
        print('-' * (int((n - 1) / 2) - x) + "*" + '-' * (x + x - 1) + "*" + '-' * (int((n - 1) / 2) - x))
    elif n % 2 == 0:
        print('-' * (int((n - 1) / 2) - x) + "*" + '-' * (x + x) + "*" + '-' * (int((n - 1) / 2) - x))

for y in range(int((n + 1) / 2) - 2, 0, -1):

    if n % 2 != 0:
        print('-' * (int((n - 1) / 2) - y) + "*" + '-' * (y + y - 1) + "*" + '-' * (int((n - 1) / 2) - y))
    elif n % 2 == 0:
        print('-' * (int((n - 1) / 2) - y) + "*" + '-' * (y + y) + "*" + '-' * (int((n - 1) / 2) - y))

    if y == 1 and n % 2 == 0:
        print('-' * (int((n-1)/2)) + "**" + '-' * (int((n-1)/2)))
    elif y == 1 and n % 2 != 0:
        print('-' * (int((n - 1) / 2)) + "*" + '-' * (int((n - 1) / 2)))

left_right = "-"
star = "*"
middle = "-"
pr
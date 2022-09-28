n = int(input())
stars = 1
left_right = int((n - stars) / 2)

for x in range(1, int((n + 1) / 2) + 1):

    middle = n - left_right * 2 - stars
    if x == 1 and n % 2 != 0:
        print('-' * left_right + "*" * stars + "-" * left_right)
        stars = 2
    elif x == 1 and n % 2 == 0:
        stars = 2
        print('-' * left_right + "*" * stars + '-' * left_right)
    else:
        print('-' * left_right + "*" * int(stars / 2) + "-" * middle + "*" * int(stars / 2) + '-' * left_right)
    left_right -= 1

left_right = 1
for y in range(int((n + 1) / 2) - 1, 0, -1):
    middle = n - left_right * 2 - stars
    if y == 1 and n % 2 != 0:
        stars = 1
        print('-' * left_right + "*" * stars + "-" * left_right)
        stars = 2
    elif y == 1 and n % 2 == 0:
        stars = 2
        print('-' * left_right + "*" * stars + '-' * left_right)
    else:
        print('-' * left_right + "*" * int(stars / 2) + "-" * middle + "*" * int(stars / 2) + '-' * left_right)
    left_right += 1
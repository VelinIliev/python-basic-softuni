n = int(input())
if n % 2 == 0:
    frame_position = int(n / 2)
else:
    frame_position = int(n / 2 + 1)

frame_first = "*" * n * 2
frame_middle = "*" + "/" * (2 * n - 2) + "*"
frame_last = "*" * n * 2
middle = " " * n
middle2 = "|" * n

for x in range(1, n + 1):
    if x == 1:
        print(frame_first + middle + frame_first)
    elif x == n :
        print(frame_last + middle + frame_last)
    elif x == frame_position :
        print(frame_middle + middle2 + frame_middle)
    else:
        print(frame_middle + middle + frame_middle)
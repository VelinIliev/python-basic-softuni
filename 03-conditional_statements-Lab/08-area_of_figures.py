from math import pi

figure = input()

if figure == "square":
    a = float(input())
    s = a * a
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    s = a * b
elif figure == "circle":
    r = float(input())
    s = pi * r * r
elif figure == "triangle":
    a = float(input())
    h = float(input())
    s = (a * h) / 2
s = round(s,3)
print(f'{s:.3f}')
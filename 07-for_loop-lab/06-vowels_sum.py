text = input()

a = 1
e = 2
i = 3
o = 4
u = 5

sum = 0

for letter in text:
    if letter == "a":
        sum = sum + a
    elif letter == "e":
        sum = sum + e
    elif letter == "i":
        sum = sum + i
    elif letter == "o":
        sum = sum + o
    elif letter == "u":
        sum = sum + u

print(sum)
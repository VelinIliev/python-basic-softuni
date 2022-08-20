number = int(input())
count = 0
password = ""
# control_value = a * b + c * d
# a < b
# c > d
for a in range(1, 10):
    for b in range(1,10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a < b and c > d and a * b + c * d == number:
                    print(f'{a}{b}{c}{d}', end = " ")
                    count += 1
                    if count == 4:
                        password = f'{a}{b}{c}{d}'
if count > 0:
    print()
if password != "":
    print(f'Password: {password}')
else:
    print("No!")


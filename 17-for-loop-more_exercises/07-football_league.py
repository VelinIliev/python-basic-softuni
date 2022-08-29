capacity_of_stadium = int(input())
number_of_fans = int(input())
sector_a = 0
sector_b = 0
sector_v = 0
sector_g = 0

for fan in range(number_of_fans):
    sector = input()
    if sector == "A":
        sector_a += 1
    elif sector == "B":
        sector_b += 1
    elif sector == "V":
        sector_v += 1
    elif sector == "G":
        sector_g += 1

print(f"{sector_a / number_of_fans * 100:.2f}%")
print(f"{sector_b / number_of_fans * 100:.2f}%")
print(f"{sector_v / number_of_fans * 100:.2f}%")
print(f"{sector_g / number_of_fans * 100:.2f}%")
print(f"{number_of_fans / capacity_of_stadium * 100:.2f}%")
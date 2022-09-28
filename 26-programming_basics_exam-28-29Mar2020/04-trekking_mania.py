number_of_groups = int(input())

musala = 0
montblan = 0
kilimandjaro = 0
k2 = 0
everest = 0

for group in range(number_of_groups):
    members = int(input())
    if members <= 5:
        musala += members
    elif members <= 12:
        montblan += members
    elif members <= 25:
        kilimandjaro += members
    elif members <= 40:
        k2 += members
    elif members > 40:
        everest += members

total_members = musala + montblan + kilimandjaro + k2 + everest
print(f'{musala / total_members * 100:.2f}%')
print(f'{montblan / total_members * 100:.2f}%')
print(f'{kilimandjaro / total_members * 100:.2f}%')
print(f'{k2 / total_members * 100:.2f}%')
print(f'{everest / total_members * 100:.2f}%')
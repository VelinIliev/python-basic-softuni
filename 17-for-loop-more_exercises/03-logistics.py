number_of_cargo = int(input())

total_tons = 0
microbus_tons = 0
truck_tons = 0
train_tons = 0
total = 0

for cargo in range(number_of_cargo):
    tons = int(input())
    total_tons += tons
    if tons <= 3:
        microbus_tons += tons
        total += tons * 200
    elif tons <= 11:
        truck_tons += tons
        total += tons * 175
    else:
        train_tons += tons
        total += tons * 120

print(f'{total / total_tons:.2f}')
print(f'{microbus_tons / total_tons * 100:.2f}%')
print(f'{truck_tons / total_tons * 100:.2f}%')
print(f'{train_tons / total_tons * 100:.2f}%')

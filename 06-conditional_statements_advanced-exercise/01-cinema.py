projection_type = input()
rows = int(input())
columns = int(input())

total_places = rows * columns

if projection_type == "Premiere":
    income = total_places * 12
elif projection_type == "Normal":
    income = total_places * 7.5
elif projection_type == "Discount":
    income = total_places * 5

print(f'{income:.2f} leva')
number_of_people = int(input())

back = 0
chest = 0
legs = 0
abs_x = 0
protein_shake = 0
protein_bar = 0
work_out = 0
protein = 0

for person in range(number_of_people):
    activity = input()
    if activity == "Back":
        back += 1
        work_out += 1
    elif activity == "Chest":
        chest += 1
        work_out += 1
    elif activity == "Legs":
        legs += 1
        work_out += 1
    elif activity == "Abs":
        abs_x += 1
        work_out += 1
    elif activity == "Protein shake":
        protein_shake += 1
        protein += 1
    elif activity == "Protein bar":
        protein_bar += 1
        protein += 1

print(f'{back} - back')
print(f'{chest} - chest')
print(f'{legs} - legs')
print(f'{abs_x} - abs')
print(f'{protein_shake} - protein shake')
print(f'{protein_bar} - protein bar')
print(f'{work_out / number_of_people * 100:.2f}% - work out')
print(f'{protein / number_of_people * 100:.2f}% - protein')

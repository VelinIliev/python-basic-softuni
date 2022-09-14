number_of_painted_eggs = int(input())

red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0

while number_of_painted_eggs > 0:
    egg_color = input()
    if egg_color == "red":
        red_eggs += 1
    elif egg_color == "orange":
        orange_eggs += 1
    elif egg_color == "blue":
        blue_eggs += 1
    elif egg_color == "green":
        green_eggs += 1
    number_of_painted_eggs -= 1

max_eggs = 0
color_of_max_eggs = ""
total_eggs = [red_eggs, orange_eggs, blue_eggs, green_eggs]
color_eggs = ["red", "orange", "blue", "green"]

for index, egg in enumerate(total_eggs):
    if egg > max_eggs:
        max_eggs = egg
        color_of_max_eggs = color_eggs[index]

print(f'Red eggs: {red_eggs}')
print(f'Orange eggs: {orange_eggs}')
print(f'Blue eggs: {blue_eggs}')
print(f'Green eggs: {green_eggs}')
print(f'Max eggs: {max_eggs} -> {color_of_max_eggs}')
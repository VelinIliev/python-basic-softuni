house_height = float(input())
house_width = float(input())
roof_height = float(input())

door = 1.2 * 2
front_wall = house_height * house_height - door
back_wall = house_height * house_height
window = 1.5 * 1.5
side_walls = (house_width * house_height - window) * 2

total_walls_area = front_wall + back_wall + side_walls

front_roof = house_height * roof_height / 2
side_roof = house_height * house_width

total_roof_area = front_roof * 2 + side_roof * 2

green_paint = total_walls_area / 3.4
red_paint = total_roof_area / 4.3

print(f'{green_paint:.2f}')
print(f'{red_paint:.2f}')
